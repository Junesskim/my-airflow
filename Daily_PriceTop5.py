import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import json

# target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)
now = datetime.now()
target_date = now - relativedelta(years=13)

dag = DAG(
    dag_id="Daily_PriceTop5",
    start_date=target_date,
    schedule_interval=None,
)

def _pricetop5(execution_date):
    year, month, day = target_date.timetuple()[:3]
    csv_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
    output_path = "/opt/airflow/output/PriceTop5_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_csv(csv_file_path)
    df = df.groupby('Country')['UnitPrice'].sum().sort_values(ascending=False).head(5)
    df.to_csv(output_path)

pricetop5 = PythonOperator(
    task_id = "pricetop5",
    python_callable=_pricetop5,
    dag = dag
)
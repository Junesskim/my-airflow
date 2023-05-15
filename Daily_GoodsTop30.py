import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime
import pandas as pd
import json

target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)

dag = DAG(
    dag_id="Daily_GoodsTop30",
    start_date=target_date,
    schedule_interval=None,
)

def _goodstop30(execution_date):
    year, month, day = target_date.timetuple()[:3]
    csv_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
    output_path = "/opt/airflow/output/GoodsTop30_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_csv(csv_file_path)
    df = df.groupby('Country')['StockCode'].count().sort_values(ascending=False).head(30)
    df.to_csv(output_path)

goodstop30 = PythonOperator(
    task_id = "goodstop30",
    python_callable=_goodstop30,
    dag = dag
)
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime
import pandas as pd
import json

target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)

dag = DAG(
    dag_id="Daily_UserTop3",
    start_date=target_date,
    schedule_interval=None,
)

def _usertop3(execution_date):
    year, month, day = target_date.timetuple()[:3]
    csv_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
    output_path = "/opt/airflow/output/UserTop3_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_csv(csv_file_path)
    df = df.groupby('CustomerID')['UnitPrice'].sum().sort_values(ascending=False).head(3)
    df.to_csv(output_path)

goodstop30 = PythonOperator(
    task_id = "usertop3",
    python_callable=_usertop3,
    dag = dag
)
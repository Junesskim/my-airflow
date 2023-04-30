from urllib import request
import datetime

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

target_date = datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc)

dag = DAG(
    dag_id = "first_dag",
    start_date = target_date,
    schedule = None,
)

def _get_data(execution_date):
    year, month, day = execution_date.timetuple()
    url = ("host.docker.internal:5000/" f"{year}"/f"{month}"/f"{day}")
    output_path = "./airflow/dags" # <- ./airflow 디렉토리가 ?
    request.urlretrieve(url, output_path)

get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    dag=dag,
)
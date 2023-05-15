from urllib import request
import datetime

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)

dag = DAG(
    dag_id = "Daily_Task",
    start_date = target_date,
    schedule_interval= None,
)

def _get_data(execution_date):
    year, month, day = target_date.timetuple()[:3]
    url = ("http://host.docker.internal:5000/"f"{year}/"f"{month}/"f"{day}")
    # url = ("http://127.0.0.1:5000/2011/11/11")
    # print(url)
    # print(execution_date)
    output_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".json" # <- ./airflow 디렉토리가 ?
    # output_path = "/home/june/airflow/output/2011-11-11.json"
    # print(output_path)
    request.urlretrieve(url, output_path)

get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    dag=dag,
)

# _get_data(target_date)
from urllib import request
import datetime

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

target_date = datetime.datetime(2021, 10, 11, tzinfo=datetime.timezone.utc)

dag = DAG(
    dag_id = "first_dag",
    start_date = target_date,
    schedule = None,
)

def _get_data(execution_date):
    year, month, day = execution_date.timetuple()[:3]
    url = ("http://127.0.0.1:5000/"f"{year}/"f"{month}/"f"{day}")
    print(url)
    output_path = "/home/june/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv" # <- ./airflow 디렉토리가 ?
    print(output_path)
    request.urlretrieve(url, output_path)

# get_data = PythonOperator(
#     task_id="get_data",
#     python_callable=_get_data,
#     dag=dag,
# )

_get_data(target_date)

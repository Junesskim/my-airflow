from urllib import request

import airflow from airflow
import DAG from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id = "first_dag",
    start_date = '2021-01-01',
    schedule_interval = None,
)

def _get_data(execution_date):
    year, month, day = execution_date.timetuple()
    url = (
        "http://127.0.0.1:5000/"
        f"{year}"/f"{month}"/f"{day}"
    )
    output_path = "./airflow/dags"
    request.urlretrieve(url, output_path)

get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    dag=dag,
)
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
    dag_id= "Daily_Read_json",
    start_date= target_date,
    schedule_interval= None,
)

def _get_file(execution_date):
    year, month, day = target_date.timetuple()[:3]
    json_file_path = ("/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}.json")
    # print(json_file_path)
    output_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
    Daily_invoice = pd.read_json(json_file_path)
    Daily_invoice.to_csv(output_path, index=False)
    # print(Daily_invoice)


get_file = PythonOperator(
    task_id = "get_file",
    python_callable=_get_file,
    dag = dag
)

# _get_file(target_date)

from urllib import request
# import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

import pandas as pd
import json

# target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)
now = datetime.now()
target_date = now - relativedelta(years=12)

dag = DAG(
    dag_id = "Daily_Invoice_Summary",
    start_date=target_date,
    schedule_interval=None,
)

def _get_data(execution_date):
    year, month, day = target_date.timetuple()[:3]
    url = ("http://host.docker.internal:5000/"f"{year}/"f"{month}/"f"{day}")
    output_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".json" # <- ./airflow 디렉토리가 ?
    request.urlretrieve(url, output_path)

# def _json_to_csv(execution_date):
#     year, month, day = target_date.timetuple()[:3]
#     json_file_path = ("/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}.json")
#     output_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
#     df = pd.read_json(json_file_path)
#     df.to_csv(output_path, index=False)

def _goodstop30(execution_date):
    year, month, day = target_date.timetuple()[:3]
    json_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".json"
    output_path = "/opt/airflow/output/GoodsTop30_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_json(json_file_path)
    df = df.groupby('Country')['StockCode'].count().sort_values(ascending=False).head(30)
    df.to_csv(output_path)


def _usertop3(execution_date):
    year, month, day = target_date.timetuple()[:3]
    json_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".json"
    output_path = "/opt/airflow/output/UserTop3_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_json(json_file_path)
    df = df.groupby('CustomerID')['UnitPrice'].sum().sort_values(ascending=False).head(3)
    df.to_csv(output_path)

def _pricetop5(execution_date):
    year, month, day = target_date.timetuple()[:3]
    json_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".json"
    output_path = "/opt/airflow/output/PriceTop5_"f"{year}-"f"{month}-"f"{day}"".csv"
    df = pd.read_json(json_file_path)
    df = df.groupby('Country')['UnitPrice'].sum().sort_values(ascending=False).head(5)
    df.to_csv(output_path)

get_data = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    dag=dag,
)

# json_to_csv = PythonOperator(
#     task_id = "get_file",
#     python_callable=_json_to_csv,
#     dag = dag,
# )

goodstop30 = PythonOperator(
    task_id = "goodstop30",
    python_callable=_goodstop30,
    dag = dag,
)

usertop3 = PythonOperator(
    task_id = "usertop3",
    python_callable=_usertop3,
    dag = dag,
)

pricetop5 = PythonOperator(
    task_id = "pricetop5",
    python_callable=_pricetop5,
    dag = dag,
)

get_data >> [goodstop30, usertop3, pricetop5]
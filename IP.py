# import airflow
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# import datetime
# from dateutil.relativedelta import relativedelta
import pandas as pd
# import json
# from urllib import request

# url = 'http://34.29.23.32:8080/log.csv'
# output_path = "/home/june/airflow/output/log.csv"

# request.urlretrieve(url, output_path)
# target_date = datetime.datetime(2011, 11, 11, tzinfo=datetime.timezone.utc)

# year, month, day = target_date.timetuple()[:3]
# csv_file_path = "/opt/airflow/output/"f"{year}-"f"{month}-"f"{day}"".csv"
csv_file_path = "/home/june/airflow/output/log.csv"
df = pd.read_csv(csv_file_path)

print(df)
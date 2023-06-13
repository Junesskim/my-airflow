import pandas as pd

csv_file_path = "/home/june/airflow/output/2011-11-11.csv"

df = pd.read_csv(csv_file_path)

df = df.groupby('CustomerID')['UnitPrice'].sum().sort_values(ascending=False).head(3)

print(df)
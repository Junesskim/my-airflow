import pandas as pd

log_csv_file_path = '/home/june/airflow/output/log.csv'

df = pd.read_csv(log_csv_file_path, sep=';')


df['Date'] = df['Date'].astype('datetime64[ns]')

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

print(df.head())

df = df.groupby(['Date', 'Host'])['Host'].count().sort_values(ascending=False)

# df['Num'] = df.sort_values(['Date', 'Host'], ascending = False).groupby(['Date']).cumcount()+1

# df = df[df['Num'] = 1]

print(df)
# df = df[df['Date'].between('2011-01-10', '2011-01-12')]

# User_json_file_path = '/home/june/airflow/output/2011-1-10.json'

# df1 = pd.read_json(User_json_file_path)

# print(df1.head())
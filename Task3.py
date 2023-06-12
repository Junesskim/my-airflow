import pandas as pd

log_csv_file_path = '/home/june/airflow/output/log.csv'

df = pd.read_csv(log_csv_file_path, sep=';')

# datetime에서 date로 변환
df['Date'] = df['Date'].astype('datetime64[ns]')

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# 원하는 집계값 만들기
df_Host = df.groupby(['Date', 'Host'])['Host'].count().sort_values(ascending=False)

df_Web = df.groupby(['Date', 'Page/File'])['Page/File'].count().sort_values(ascending=False).reset_index(name='CNT')

# 일자별 IP 사용 횟수
print(df_Host)

# rank 함수로 일자별 CNT별 순위 구하기
df_Web['Rank'] = df_Web.groupby('Date')['CNT'].rank(method='max', ascending=False)

df_Web['Rank'] = pd.to_numeric(df_Web['Rank'], downcast='integer')

df_Web = df_Web[df_Web['Rank'] <= 10]

# 일자별 방문 페이지 TOP 10
print(df_Web)

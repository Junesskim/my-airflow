import pandas as pd

csv_file_path = "/home/june/airflow/output/2011-11-11.csv"

df = pd.read_csv(csv_file_path)

df['CustomerID'] = pd.to_numeric(df['CustomerID'], downcast= 'integer')

df_Top3 = df.groupby('CustomerID')['UnitPrice'].sum().sort_values(ascending=False).head(3).reset_index(name='TotalPrice')

df_Top3['CustomerID'] = pd.to_numeric(df_Top3['CustomerID'], downcast='integer')

# print(df_Top3.CustomerID[0])

# print(df[df.CustomerID == df_Top3.CustomerID[0]])

df_first = df[df.CustomerID == df_Top3.CustomerID[0]]

# print(df_first)

# InvoiceNo 에 따른 UnitPrice의 합
df_first_unitprice_invoiceno = df_first.groupby('InvoiceNo')['UnitPrice'].sum().sort_values(ascending=False).reset_index(name='InvoiceSumPrice')

# InvoiceNo 에 따른 구매 물품 갯수
df_first_count_invoiceno = df_first.groupby('InvoiceNo')['StockCode'].count().sort_values(ascending=False).reset_index(name='StockCount')

print(df_first_unitprice_invoiceno)

print(df_first_count_invoiceno)

df_first_invoice = pd.merge(df_first_count_invoiceno, df_first_unitprice_invoiceno, on='InvoiceNo')

print(df_first_invoice)
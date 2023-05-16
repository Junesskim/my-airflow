import pandas as pd
import json

json_file_path = '/home/june/airflow/output/2011-11-11.json'


# with open(json_file_path, 'r') as f:
#     contents = json.load(f)

# print(len(contents))
Daily_Invoice = pd.read_json(json_file_path)

# InvoiceNo = []
# StockCode = []
# Description =[]
# Quantity = []
# InvoiceDate = []
# UnitPrice = []
# CustomerID = []
# Country = []

# for i in range(len(contents)):
#     InvoiceNo.append(contents[i]['InvoiceNo'])
#     StockCode.append(contents[i]['StockCode'])
#     Description.append(contents[i]['Description'])
#     Quantity.append(contents[i]['Quantity'])
#     InvoiceDate.append(contents[i]['InvoiceDate'])
#     UnitPrice.append(contents[i]['UnitPrice'])
#     CustomerID.append(contents[i]['CustomerID'])
#     Country.append(contents[i]['Country'])

# Daily_Invoice = pd.DataFrame({'InvoiceNo' : InvoiceNo, 
#                               'StockCode' : StockCode,
#                               'Description' : Description,
#                               'Quantity' : Quantity,
#                               'InvoiceDate' : InvoiceDate,
#                               'UnitPrice' : UnitPrice,
#                               'CustomerID' : CustomerID,
#                               'Country' : Country
#                               })

# print(Daily_Invoice.head())

print(Daily_Invoice.groupby('Country')['StockCode'].count().sort_values(ascending=False).head(30))

# print(Daily_Invoice.groupby('CustomerID')['UnitPrice'].sum().sort_values(ascending=False).head(3))

# print(Daily_Invoice.groupby('Country')['UnitPrice'].sum().sort_values(ascending=False).head(5))

# Daily_Invoice_Count = Daily_Invoice.groupby('Country')['StockCode'].count()

# print(Daily_Invoice_Count.sort_values(ascending=False))
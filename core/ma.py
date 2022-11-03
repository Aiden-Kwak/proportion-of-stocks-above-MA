import FinanceDataReader as fdr
import datetime
import pandas as pd

today = datetime.date.today()
start = today - datetime.timedelta(days=21)
csv_sp500 = pd.read_csv('../csv/SP500.csv',\
                 names=['', 'Symbol', 'Name', 'Sector', 'Industry'],\
                 encoding='utf-8')

csv_nasdaq = pd.read_csv('../csv/NASDAQ.csv',\
                 names=['', 'Symbol', 'Name', 'Industry', 'IndustryCode'],\
                 encoding='utf-8')

csv_kospi = pd.read_csv('../csv/KOSPI.csv',\
                 names=['', 'Code', 'ISU_CD', 'Name', 'Market', 'Dept', 'Close', 'ChangeCode', 'Changes', 'ChagesRatio', 'Open', 'High', 'Low', 'Volume', 'Amount', 'Marcap', 'Stocks', 'MarketId'],\
                 encoding='utf-8')

csv_kosdaq = pd.read_csv('../csv/KOSDAQ.csv',\
                 names=['', 'Code', 'ISU_CD', 'Name', 'Market', 'Dept', 'Close', 'ChangeCode', 'Changes', 'ChagesRatio', 'Open', 'High', 'Low', 'Volume', 'Amount', 'Marcap', 'Stocks', 'MarketId'],\
                 encoding='utf-8')


sp500_list = csv_sp500['Symbol'].values.tolist()
nasdaq_list = csv_nasdaq['Symbol'].values.tolist()
kospi_list = csv_kospi['Code'].values.tolist()
kosdaq_list = csv_kosdaq['Code'].values.tolist()

print(sp500_list)
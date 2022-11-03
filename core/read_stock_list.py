import FinanceDataReader as fdr
import pandas as pd

nasdaq = fdr.StockListing('NASDAQ')
sp500 = fdr.StockListing('SP500')
kospi = fdr.StockListing('KOSPI')
kosdaq = fdr.StockListing('KOSDAQ')
nasdaq.to_csv('../csv/NASDAQ.csv')
sp500.to_csv('../csv/SP500.csv')
kospi.to_csv('../csv/KOSPI.csv')
kosdaq.to_csv('../csv/KOSDAQ.csv')
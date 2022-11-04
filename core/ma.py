import FinanceDataReader as fdr
import datetime
import time
import pandas as pd

today = datetime.date.today()
start_100 = today - datetime.timedelta(days=101)
start_20 = today - datetime.timedelta(days=21)
start_10 = today - datetime.timedelta(days=11)


class get_all_list:
    def sp500_list():
        csv_sp500 = pd.read_csv('../csv/SP500.csv',\
                        names=['', 'Symbol', 'Name', 'Sector', 'Industry'],\
                        encoding='utf-8')

        return csv_sp500['Symbol'].values.tolist()

    def nasdaq_list():
        csv_nasdaq = pd.read_csv('../csv/NASDAQ.csv',\
                        names=['', 'Symbol', 'Name', 'Industry', 'IndustryCode'],\
                        encoding='utf-8')

        return csv_nasdaq['Symbol'].values.tolist()
        
    def kospi_list():
        csv_kospi = pd.read_csv('../csv/KOSPI.csv',\
                        names=['', 'Code', 'ISU_CD', 'Name', 'Market', 'Dept', 'Close', 'ChangeCode', 'Changes', 'ChagesRatio', 'Open', 'High', 'Low', 'Volume', 'Amount', 'Marcap', 'Stocks', 'MarketId'],\
                        encoding='utf-8')
        
        return csv_kospi['Code'].values.tolist()
        
    def kosdaq_list():
        csv_kosdaq = pd.read_csv('../csv/KOSDAQ.csv',\
                        names=['', 'Code', 'ISU_CD', 'Name', 'Market', 'Dept', 'Close', 'ChangeCode', 'Changes', 'ChagesRatio', 'Open', 'High', 'Low', 'Volume', 'Amount', 'Marcap', 'Stocks', 'MarketId'],\
                        encoding='utf-8')

        return csv_kosdaq['Code'].values.tolist()


class functions:
    
    def get_ma_10(code):
        global cnt, total, price_list
        price_sum = 0
        price_df = fdr.DataReader(code, start=start_100, end=today)   
        try:
            price_list = price_df['Close'].values.tolist()
            cnt+=1
        except:
            print('key error occured')
            total-=1
            time.sleep(2)
        for i, price in enumerate(price_list[::-1]):
            if i==0:
                price_sum = price
            elif i<=9:
                price_sum += price
            else:
                pass
        
        ma = price_sum/10

        return ma
    
    def get_today_price(code):
        today_price = price_list[-1]
        return today_price

if __name__ == '__main__':
    above_ma_list = list()


    # <<<<<<< KOSDAQ >>>>>>
    # kosdaq_list = get_all_list.kosdaq_list()
    # cnt = 0
    # total = len(kosdaq_list)-1
    # aboved_item = 0
    # for code in kosdaq_list[1:]:
    #     ma = functions.get_ma_10(code)
    #     now_price = functions.get_today_price(code)
    #     if now_price > ma:
    #         above_ma_list.append(code)
    #         aboved_item+=1

    #     print(code+'| 진행도 '+' ===> '+'['+str(cnt)+'/'+str(total)+']'+','+str(aboved_item))

    # <<<<<<< KOSPI >>>>>>
    # kospi_list = get_all_list.kospi_list()
    # cnt = 0
    # total = len(kospi_list)-1
    # aboved_item = 0
    # for code in kospi_list[1:]:
    #     ma = functions.get_ma_10(code)
    #     now_price = functions.get_today_price(code)
    #     if now_price > ma:
    #         above_ma_list.append(code)
    #         aboved_item+=1

    #     print(code+'| 진행도 '+' ===> '+'['+str(cnt)+'/'+str(total)+']'+','+str(aboved_item))


    # <<<<<<< S&P500 >>>>>>
    sp500_list = get_all_list.sp500_list()
    cnt = 0
    total = len(sp500_list)-1
    aboved_item = 0
    for code in sp500_list[1:]:
        ma = functions.get_ma_10(code)
        now_price = functions.get_today_price(code)
        if now_price > ma:
            above_ma_list.append(code)
            aboved_item+=1

        print(code+'| 진행도 '+' ===> '+'['+str(cnt)+'/'+str(total)+']'+','+str(aboved_item))


    # <<<<<<< NASDAQ >>>>>>
    # nasdaq_list = get_all_list.nasdaq_list()
    # cnt = 0
    # total = len(nasdaq_list)-1
    # aboved_item = 0
    # for code in nasdaq_list[1:]:
    #     ma = functions.get_ma_10(code)
    #     now_price = functions.get_today_price(code)
    #     if now_price > ma:
    #         above_ma_list.append(code)
    #         aboved_item+=1

    #     print(code+'| 진행도 '+' ===> '+'['+str(cnt)+'/'+str(total)+']'+','+str(aboved_item))
    

    print(str(round((aboved_item/total)*100))+'%의 종목이 이평선 위에 있습니다.')
    print(above_ma_list)



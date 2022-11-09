import FinanceDataReader as fdr
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt

today = datetime.date.today()
df_sp500 = fdr.DataReader('US500', '2022-10-03', today)
index = df_sp500.index.tolist()
조정값 = [85.6, 93.4, 90.2, 87.2, 90.8, 91, 87.6, 55, 45, 57.8, 61, 67.9] # 최우측이 오늘
ma_list = [0]*(len(index)-len(조정값))+조정값

df_ma = pd.DataFrame({'ma':ma_list, 'Date':index})
df_ma.set_index('Date', inplace=True)
print(df_sp500)
print(df_ma)


fig, ax1 = plt.subplots()
color_1 = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Index (blue)', fontsize=14, color=color_1)
ax1.plot(df_sp500['Close'], color=color_1)
ax1.tick_params(axis='y', labelcolor=color_1)

ax2 = ax1.twinx()
color_2 = 'tab:red'
ax2.set_ylabel('Proportion of stocks (red)', fontsize=14, color=color_2)
ax2.plot(df_ma['ma'], color=color_2)
ax2.tick_params(axis='y', labelcolor=color_2)

fig.tight_layout()
plt.savefig('test.png')
plt.show(block=True)
# auther:杨亚虎
# encoding:utf-8
# 导入必要的模块和类
import csv
from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib import dates as mdates

def get_weather_data(filename, dates, highs, lows):
    """从文件中获取日期、最高气温和最低气温"""

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d") # strptime():根据指定的格式把一个时间字符串解析为时间元组 
                high = int(row[1])
                low = int(row[3])
            
            except ValueError:
                print(current_date, 'missing date')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        
# 锡特卡气温
dates, highs, lows = [], [], []
filename = '/home/yyh/Documents/VSCode_work/chapter16/sitka_weather_2014.csv'
get_weather_data(filename, dates, highs, lows) 

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# 死亡谷气温
dates, highs, lows = [], [], []
filename = '/home/yyh/Documents/VSCode_work/chapter16/death_valley_2014.csv'
get_weather_data(filename, dates, highs, lows) 

# 根据数据绘制图形
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nSitka, AK and Death Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', top=True, right=True, which='both', labelsize=16)
plt.ylim(10, 120)
plt.xlim(dates[0], dates[-1]) # 这样也可以的
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # 日期格式，%B为月份名，%b为月份名缩写

# plt.show()
plt.savefig("/home/yyh/Documents/VSCode_work/chapter16/chapter16_16_2_2", bbox_inches='tight')
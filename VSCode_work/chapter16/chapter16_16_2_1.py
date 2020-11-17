# 导入必要的模块
import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

# 从文件中获取日期、最高气温和最低气温
filename = '/home/yyh/Documents/VSCode_work/chapter16/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', top=True, right=True, which='both', labelsize=16)
plt.ylim(10, 120)
plt.xlim(dates[0], dates[-1]) # 这样也可以的
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # 日期格式，%B为月份名，%b为月份名缩写

# plt.show()
plt.savefig("/home/yyh/Documents/VSCode_work/chapter16/chapter16_16_2_1", bbox_inches='tight')
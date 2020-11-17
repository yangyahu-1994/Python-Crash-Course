# 导入模块
import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

# Get dates and rainfall data from data file.
# Rainfall data is in column 19.
filename = '/home/yyh/Documents/VSCode_work/chapter16/sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls, totals = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
            if totals:
                totals.append(totals[-1] + rainfall)
            else:
                totals.append(rainfall)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

plt.plot(dates, totals, c='blue', alpha=0.75)
plt.fill_between(dates, totals, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily rainfall amounts and cumulative rainfall - 2015\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', top=True, right=True, which='both', labelsize=16)
plt.ylim(0, 120)
plt.xlim(dates[0], dates[-1]) # 这样也可以的
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # 日期格式，%B为月份名，%b为月份名缩写

# plt.show()
plt.savefig("/home/yyh/Documents/VSCode_work/chapter16/chapter16_16_4", bbox_inches='tight')
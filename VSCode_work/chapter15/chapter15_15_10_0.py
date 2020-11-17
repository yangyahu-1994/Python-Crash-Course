from die import Die
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches # 导入matplotlib标准库中的patches模块
 
 
die_1 = Die()
die_2 = Die(10)
 
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies =[]
max_results = die_1.num_sides + die_2.num_sides
X_Range = list(set(results)) # set()函数：创建一个无序不重复元素的集合
for value in X_Range:
    frequency = results.count(value)
    frequencies.append(frequency)
 
plt.bar(X_Range, frequencies, color='blue', align='center') # plt.bar()函数绘制柱状图
plt.xticks(X_Range) # plt.xticks()函数把坐标轴变成自己想要的样子
 
plt.xlabel("Results", fontsize=8)
plt.ylabel("Frequencies", fontsize=8)
 
#图例
blue_patch = mpatches.Patch(color='blue', label='D6+D6') # matplotlib.patches.Patch: 色块
plt.legend(handles=[blue_patch]) # plt.legend()函数用于创建图例

plt.show()
 
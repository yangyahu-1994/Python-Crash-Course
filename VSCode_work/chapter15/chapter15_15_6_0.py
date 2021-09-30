# 导入必要的模块和类
import pygal

from die import Die

# 创建一个D6实例
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
# 将用来设置hist.x_labels值的列表替换为一个自动生成这种列表的循环
# hist.x_labels = ['1','2', '3', '4', '5', '6']
x_l = []
for value in range(1, die.num_sides+1):
    x_l.append(str(value))
hist.x_labels = x_l
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('chapter15/result/die_visual_15_6_0.svg')
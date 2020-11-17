# 导入必要的模块和类
from die import Die
import pygal

# 创建两个D8实例
die_1 = Die(8)
die_2 = Die(8)

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [str(value) for value in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('/home/yyh/Documents/VSCode_work/chapter15/dice_visual_15_7.svg')
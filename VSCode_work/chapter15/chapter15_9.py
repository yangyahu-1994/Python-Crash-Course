# 导入必要的模块和类
from die import Die
import pygal

# 创建两个D6实例
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    if results.count(value):
        frequency = results.count(value)
        frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
# 检查一下1到max_result+1中的value是否在results列表中
x_l = []
for value in range(1, max_result+1):
    if value in results:
        x_l.append(value)
hist.x_labels = x_l
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('/home/yyh/Documents/VSCode_work/chapter15/dice_visual_15_9.svg')
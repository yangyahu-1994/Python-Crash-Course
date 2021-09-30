# 导入必要的模块
import matplotlib.pyplot as plt

# x_values = list(range(1, 6))
x_values = list(range(1, 5001))
# y_values = [x**3 for x in x_values] # 列表解析
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap= plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Cube Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# 设置每个坐标轴的取值范围
# plt.axis([1, 5, 1, 125])
plt.axis([1, 5000, 1, 125000000000])

# plt.savefig('/home/yyh/Documents/VSCode_work/chapter15/cobes_plot_1.png', bbox_inches='tight')
plt.savefig('chapter15/result/cobes_plot_3.png', bbox_inches='tight')


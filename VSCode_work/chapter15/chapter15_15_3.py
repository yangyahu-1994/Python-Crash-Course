# rw_visual.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步、
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # plt.show()
    plt.savefig('/home/yyh/Documents/VSCode_work/chapter15/random_walk_15_5.png', bbox_inches='tight')

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
# 确认一下随机漫步包含的点是否是5000
print(len(rw.x_values))
print(len(rw.y_values))
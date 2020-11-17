# 导入必要的模块和类
import pygal
from random_walk import RandomWalk
 
rw = RandomWalk(1000)
rw.fill_walk()
 
xy_chart = pygal.XY(stroke = False)  # stroke=False散点不连线
xy_chart.title = 'RandomWalk'
pygal.Line(include_x_axis = False, include_y_axis = False)
 
#把生成的值变成坐标
xy_list = []
for (x,y) in zip(rw.x_values,rw.y_values):
    xy_list.append((x,y))
 
xy_chart.add('data', xy_list)
 
xy_chart.render_to_file('/home/yyh/Documents/VSCode_work/chapter15/RandomWalk_15_10_1.svg')
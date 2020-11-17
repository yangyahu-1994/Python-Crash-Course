# 导入模块
import csv
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
 
# 加载数据
filename = '/home/yyh/Documents/VSCode_work/chapter16/children_out_school.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
    # 创建一个空字典
	children_numbers = {}
	for row in reader:
		try:
			country_name = row[0]
			children_number = int(row[62])
		except ValueError:
			print(country_name, 'missing data')
		else:
			code = get_country_code(country_name)
			if code:
				children_numbers[code] = children_number
 

# 根据数量将所有的国家分成三组
children_number_1, children_number_2, children_number_3 = {}, {}, {}
for i, value in children_numbers.items():
	if value < 1000:
		children_number_1[i] = value
	elif value < 10000:
		children_number_2[i] = value
	else:
		children_number_3[i] = value

# 看看每组分别包含多少个国家
print(len(children_number_1), len(children_number_2), len(children_number_3))

wm_style = RS('#d95e07', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'Children Out School in 2018, by Country'
wm.add('0-1000', children_number_1)
wm.add('1000-10000', children_number_2)
wm.add('>10000', children_number_3)

wm.render_to_file('/home/yyh/Documents/VSCode_work/chapter16/children_numbers.svg')
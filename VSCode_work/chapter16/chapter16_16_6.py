# 导入必要的模块
import json
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
 
# 将数据加载到列表中
filename = '/home/yyh/Documents/VSCode_work/chapter16/gdp_json.json'
with open(filename) as file_object:
	gdp_data = json.load(file_object)

# 创建一个包含gdp数据的空字典
cc_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2016:
		country = gdp_dict['Country Name']
		gdpValue = int(float(gdp_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_gdp[code] = gdpValue
 
# 根据gdp将所有的国家分成三组
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
	if gdp < 10000000000:
		cc_gdp_1[cc] = gdp
	elif gdp < 500000000000:
		cc_gdp_2[cc] = gdp
	else:
		cc_gdp_3[cc] = gdp

# 看看每组分别包含多少个国家
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))

wm_style = RS('#d95e07', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('0-10bn', cc_gdp_1)
wm.add('10bn-500bn', cc_gdp_2)
wm.add('>500bn', cc_gdp_3)

wm.render_to_file('/home/yyh/Documents/VSCode_work/chapter16/world_gdp.svg')
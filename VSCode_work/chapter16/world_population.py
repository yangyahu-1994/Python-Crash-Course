# 导入必要的模块
import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import RotateStyle

# 将数据加载到列表中
filename = '/home/yyh/Documents/VSCode_work/chapter16/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}    
for pop_dict in pop_data: # 将每个字典依次存储在pop_dict中 
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        print(country)
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        print(code)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal_maps_world.maps.World()
wm_style = RotateStyle('#336699') # 创建实例
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('/home/yyh/Documents/jupyter_work/world_population_3.svg')
# 创建字典
cities = {
    'beijing': {
        'country': 'china',
        'population': '1100000',
        'fact': 'capital',
        },
    'shanghai': {
        'country': 'china',
        'population': '122434',
        'fact': 'financial',
        },
    'hangzhou': {
        'country': 'china',
        'population': '123443',
        'fact': 'digital',
        },
    }

# 打印信息
for city, city_infos in cities.items():
    print("\nCity: " + city.title())
    for x, y in city_infos.items():
        print("\t" + x.title() + ": " + y.title())
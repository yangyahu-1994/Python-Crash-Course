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
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for x, y in city_info.items():
        print(f"\t{x.title()}: {y.title()}")
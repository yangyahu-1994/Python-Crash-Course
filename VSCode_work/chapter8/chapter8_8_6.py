# 定义函数
def city_country(city, country):
    """返回一个城市所属于的国家"""
    full = f"{city}, {country}"
    return full.title()

full_1 = city_country('beijing', 'china')
print(full_1)
full_2 = city_country('hangzhou', 'china')
print(full_2)
full_3 = city_country('shanghai', 'china')
print(full_3)
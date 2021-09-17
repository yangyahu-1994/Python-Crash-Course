# 定义函数
def describe_city(city_name, city_country="china"):
    """描述一个城市所属于的国家"""
    print(f"{city_name.title()} is in {city_country.title()}.")

describe_city('beijing')
describe_city("hangzhou")
describe_city(city_name='roma')
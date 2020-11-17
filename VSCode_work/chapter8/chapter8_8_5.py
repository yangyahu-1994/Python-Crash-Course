# 定义函数
def describe_city(city_name, city_country = "china"):
    print(city_name.title() + " is in " + city_country.title() + ".")

describe_city('beijing')
describe_city("hangzhou")
describe_city(city_name = 'roma')
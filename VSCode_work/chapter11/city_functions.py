# 定义一个函数
def get_city_country(city, country, population=''):
    """返回一个格式为City, Country - population xxx 的字符串"""
    if population:
        formatted_city_country = f"{city.title()}, {country.title()} - population {population}" 
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country
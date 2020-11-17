from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Zimbabwe':
        return 'zw'
    elif country_name == 'Zambia':
        return 'zm'
    elif country_name == 'Viet Nam':
        return 'vn'
    elif country_name == 'Venezuela, Bolivarian Republic of':
        return 've'
        
    # 如果没有找到指定的国家，就返回None
    return None
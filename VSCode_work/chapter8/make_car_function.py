# 定义函数
def make_car(manufacturer, model, **car_info):
    """创建一个字典，将一辆汽车的相关信息包括其中"""
    profile = {}
    profile['car_manufacturer'] = manufacturer
    profile['car_model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile
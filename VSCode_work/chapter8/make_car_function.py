# 定义函数
def make_car(manufacturer, model, **car_info):
    """创建一个字典，将一辆汽车的相关信息包括其中"""
    car_info['car_manufacturer'] = manufacturer
    car_info['car_model'] = model
    return car_info
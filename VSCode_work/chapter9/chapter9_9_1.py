# 创建类
class Restaurant():
    """创建一个实例，分别打印其两个属性，再调用两个方法"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化restaurant的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        print(self.restaurant_name)
        print(self.cuisine_type)

    def describe_restraurant(self):
        """描述餐馆"""
        print("\nThe name of this restaurant is " + self.restaurant_name.title() + ".")
        print("The type of cuisine in this restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """打开餐馆"""
        print("The restaurant is open.")

restaurant = Restaurant('Tianrun Tofu Fanzhuang', 'Cantonese')

restaurant.describe_restraurant()
restaurant.open_restaurant()



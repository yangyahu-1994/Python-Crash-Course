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
        print(f"\nThe name of this restaurant is {self.restaurant_name.title()}.")
        print(f"The type of cuisine in this restaurant is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """打开餐馆"""
        print("The restaurant is open.")

# 基于类创建实例
restaurant_0 = Restaurant('Tianrun Tofu Fanzhuang', 'Cantonese')
restaurant_1 = Restaurant('Tianyuan Club Cantonese Restaurant', 'Sichuan cuisine')
restaurant_2 = Restaurant('Delicious home cooking in Jincaifu', 'Chengdu cuisine')

# 调用方法
restaurant_0.describe_restraurant()
restaurant_1.describe_restraurant()
restaurant_2.describe_restraurant()
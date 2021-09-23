# 创建类
class Restaurant():
    """创建一个实例，分别打印其两个属性，再调用两个方法"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化restaurant的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restraurant(self):
        """描述餐馆"""
        print(f"The name of this restaurant is {self.restaurant_name.title()}.")
        print(f"The type of cuisine in this restaurant is {self.cuisine_type.title()}.")
        print(f"A total of {self.number_served} people have eaten in this restaurant.")

    def open_restaurant(self):
        """打开餐馆"""
        print("The restaurant is open.")

    def set_number_served(self, number_of_peaple_eat):
        """设置就餐人数"""
        self.number_served = number_of_peaple_eat

    def increment_number_served(self, increased_number):
        """将就餐人数递增"""
        self.number_served += increased_number


class IceCreamStand(Restaurant):
    """冰淇淋小店的一次简单尝试"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        冰淇淋小店的独特之处
        初始化父类属性和冰淇淋小店特有的属性
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Oreo','milk','banana']

    def describe_flavors(self):
        """显示这些冰淇淋"""
        for flavor in self.flavors:
            print(f"The flavor is {flavor}.")
            
# 创建实例
my_ice_cream_shop = IceCreamStand('Tianrun Tofu Fanzhuang', 'Cantonese')

# 调用方法
my_ice_cream_shop.describe_flavors()
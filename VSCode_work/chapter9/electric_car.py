"""一组可用于表示电动汽车的类"""

from car import Car

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = f"This car can go approximately {range} miles on a full charge"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        +"""
        super().__init__(make, model, year)
        self.battery = Battery()
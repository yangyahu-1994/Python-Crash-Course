# 从模块导入函数
from random import randint

# 创建类
class Die():
    """一次简单尝试"""

    def __init__(self, sides=6):
        """初始化属性"""
        self.sides = sides

    def roll_die(self):
        """打印位于1和骰子面数之间的随机数"""
        x = randint(1, self.sides)
        print(x)

# 创建一个6面的骰子，掷10次
print("------创建一个6面的骰子，掷10次----------")
six_die = Die()
for number in range(1,11):
    six_die.roll_die()

# 创建一个10面的骰子，掷10次
print("--------创建一个10面的骰子，掷10次---------")
ten_die = Die(10)
for number in range(1, 11):
    ten_die.roll_die()

# 创建一个20面的骰子，掷10次
print("--------创建一个20面的骰子，掷10次---------")
ten_die = Die(20)
for number in range(1, 11):
    ten_die.roll_die()
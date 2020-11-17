# 定义类
class Employee():
    """一次简单尝试"""

    def __init__(self, first_name, last_name, annual_salary):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_salary_increment=5000):
        """
        默认将年薪增加5000美元
        ，但也能够接受其他的年薪增加量
        """
        self.annual_salary += annual_salary_increment
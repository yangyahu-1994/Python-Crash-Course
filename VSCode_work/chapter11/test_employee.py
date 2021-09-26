# 导入必要的模块和要测试的类
import unittest
from employee import Employee

# 定义测试用例
class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建新的雇员实例和属性，供使用的测试方法使用"""
        self.my_employee = Employee('yahu', 'yang', 65000)

    def test_give_default_raise(self):
        """测试默认加薪"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 70000)

    def test_give_custom_raise(self):
        """测试自定义加薪"""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 75000)

if __name__ == '__main__':
    unittest.main()
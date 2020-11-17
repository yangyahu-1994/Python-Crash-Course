# 导入必要的模块和要测试的函数
import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """测试city_functions.py"""
    
    def test_city_country(self):
        """无population的测试"""
        my_city = get_city_country('beijing', 'china')
        self.assertEqual(my_city, 'Beijing, China')

    def test_city_country_population(self):
        """有population的测试"""
        my_city = get_city_country('beijing', 'china', population='50000000')
        self.assertEqual(my_city, 'Beijing, China - population 50000000')

unittest.main()
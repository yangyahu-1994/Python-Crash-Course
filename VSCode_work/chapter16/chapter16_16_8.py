# 导入模块
import unittest
from country_codes import get_country_code

class TestCountryCodes(unittest.TestCase):
    """测试get_country_code()"""
    
    def test_get_country_code(self):
        """能否正确地返回两位国别码?"""
        code = get_country_code("Andorra")
        self.assertEqual(code, "ad")

unittest.main()


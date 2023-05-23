import unittest
from ddt import ddt, data, unpack
import time

test_data = [
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},
    {"user": "admin6", "psw": "1234", "result": "true"},
    {"user": "admin7", "psw": "1234", "result": "true"},
    {"user": "admin8", "psw": "1234", "result": "true"},
    {"user": "admin9", "psw": "1234", "result": "true"},
    {"user": "admin10", "psw": "1234", "result": "true"},
    {"user": "admin11", "psw": "1234", "result": "true"}
]

@ddt
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = test_data

    @data(*test_data)
    @unpack
    def test_case01(self, user, psw, result):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % user)
        print("输入密码：%s" % psw)
        print("期望结果：%s " % result)
        time.sleep(0.5)
        self.assertTrue(result == "true")

if __name__ == '__main__':
    unittest.main(verbosity=2)
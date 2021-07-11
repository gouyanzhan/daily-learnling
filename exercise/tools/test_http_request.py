import unittest
from exercise.tools.http_request import HttpRequest
from exercise.tools.get_cookie import GetCookie
from ddt import ddt,data  #列表嵌套列表或者是列表嵌套字典
from exercise.tools.da_excel import DoExcel

test_data = DoExcel.get_data("../test_data/test_data.xlsx",'login') #执行登录的用例
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        login_data = {"mobilephone": "15096098888", "pwd": "123456"}
        res = HttpRequest.http_request(item['url'],item['data'],"post",getattr(GetCookie,"Cookie"))
        print("获取到的结果是：{0}".format(res.json()))



    def tearDown(self):
        pass
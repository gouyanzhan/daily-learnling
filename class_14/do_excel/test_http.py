import unittest

import self as self

from class_14.do_excel.get_data import GetData
from class_14.do_excel.http_request import HttpRequest
from ddt import ddt,data
from class_14.do_excel.do_excel import DoExcel
#列表里面嵌套了字典

test_data = DoExcel("test3.xlsx","python").get_data()
@ddt
class TestHttp(unittest.TestCase):
    def setUp(self):  #重写
        print("开始测试啦")

    @data(*test_data)
    def test_api(self,item):  #接口用例
            res = HttpRequest().http_request(item["url"],eval(item["data"]),item["method"],getattr(GetData,"Cookie"))
            if res.cookies:    #如果cookie有的话，就更新COOKIE
                setattr(GetData,"Cookie")
            try:
                self.assertEquals(item["expected"],res.json()["code"])
            except AssertionError as e:
                print("test_api's error is{}".format(e))
                raise e
            print(res.json())

    def tearDown(self):
        pass

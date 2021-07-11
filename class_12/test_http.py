import unittest

import self as self

from class_12.get_data import GetData
from class_12.http_request import HttpRequest
#列表里面嵌套了字典


class TestHttp(unittest.TestCase):
    def setUp(self):
        pass

    def __init__(self,methodName,url,data,method,expected): # 通过初始化函数来传参数
        super(TestHttp, self).__init__(methodName)  #超继承：父类的方法保留了
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    def test_api(self):  #接口用例
            res = HttpRequest().http_request(self.url,self.data,self.method,getattr(GetData,"Cookie"))
            if res.cookies:    #如果cookie有的话，就更新COOKIE
                setattr(GetData,"Cookie")
            try:
                self.assertEquals(self.expected,res.json()["code"])
            except AssertionError as e:
                print("test_api's error is{}".format(e))
                raise e
            print(res.json())

    # def test_login_wrong_pwd(self):
    #     res = HttpRequest().http_request(self.login_url,data,'get')
    #     try:
    #         self.assertEquals("20111", res.json()["code"])
    #     except AssertionError as e:
    #         print("test_login_normal's error is{}".format(e))
    #         raise e
    #
    # def test_recharge_normal(self):
    #     res = HttpRequest().http_request(self.recharge_url,recharge_data,'post',getattr(GetData,"Cookie"))
    #     try:
    #         self.assertEquals("10001",res.json()["code"])
    #     except AssertionError as e:
    #         print("test_recharge_normal's error is{}".format(e))
    #         raise e
    # def test_recharge_negative(self):
    #     # res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post',COOKIE)
    #     res = HttpRequest().http_request(self.recharge_url,recharge_data,'post',getattr(GetData,"Cookie"))
    #     try:
    #         self.assertEquals("20117",res.json()["code"])
    #     except AssertionError as e:
    #         print("test_recharge_normal's error is{}".format(e))
    #         raise e
    def tearDown(self):
        pass

#1：全局变量  局部变量   如果要修改全局变量的值  怎么去改
#缺点：关联性比较强 一步错步步错

#2:反射

#3：setUp

import unittest
from API_AUTO.tools.http_requests import HttpRequest
from class_11.get_data import GetData
# COOKIE = None #全局变量
class TestHttp(unittest.TestCase):
    def setUp(self):
        # 登录
        self.login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        # self.login_data = {"mobilephone": "1310000000", "pwd": "123456"}
        #充值的url
        self.recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
        # #获取登录后的cookies
        # self.cookies = HttpRequest().http_request(self.login_url,self.login_data,'get').cookies
        print("setup函数里面登录后产生的cookies是：{}".format(self.cookies))
    def test_login_normal(self):  #正常登录
        global COOKIE #声明全局变量
        data = {"mobilephone": "1310000000", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url,data,'get')
        if res.cookies:    #如果cookie有的话，就更新COOKIE
            # COOKIE = res.cookies
            setattr(GetData,"Cookie")

        try:
            self.assertEquals("10001",res.json()["code"])
        except AssertionError as e:
            print("test_login_normal's error is{}".format(e))
            raise e

    def test_login_wrong_pwd(self):
        data = {"mobilephone": "1310000000", "pwd": "123456789"}
        res = HttpRequest().http_request(self.login_url,data,'get')
        try:
            self.assertEquals("20111", res.json()["code"])
        except AssertionError as e:
            print("test_login_normal's error is{}".format(e))
            raise e

    def test_recharge_normal(self):
        global COOKIE
        recharge_data = {"mobilephone": "18688773467", "amount": "2000"}
        res = HttpRequest().http_request(self.recharge_url,recharge_data,'post',COOKIE)
        try:
            self.assertEquals("10001",res.json()["code"])
        except AssertionError as e:
            print("test_recharge_normal's error is{}".format(e))
            raise e
    def test_recharge_negative(self):
        # global COOKIE
        recharge_data = {"mobilephone": "18688773467", "amount": "-1000"}
        # res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post',COOKIE)
        res = HttpRequest().http_request(self.recharge_url,recharge_data,'post',getattr(GetData,"Cookie"))
        try:
            self.assertEquals("20117",res.json()["code"])
        except AssertionError as e:
            print("test_recharge_normal's error is{}".format(e))
            raise e
    def tearDown(self):
        pass

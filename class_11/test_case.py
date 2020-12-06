import unittest
import requests

log_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

class HttpRequest:
    def __init__(self,url,method,data=None,cookies=None):
        self.url = url
        self.method = method
        self.data = data
        self.cookies = cookies
    def http_request(self):
        self.method = self.method.upper()
        if self.method == "GET":
            res = requests.get(self.url,data = self.data,cookies = self.cookies,verify = False)
            return res
        elif self.method == "POST":
            res = requests.post(self.url, data=self.data, cookies=self.cookies, verify=False)
            return res
        else:
            raise Exception("不支持的请求")


# 登陆接口
class Login(unittest.TestCase):
    #正常登陆
    def test_01(self):
        log_data = {"mobilephone":"18688773467",
                    "pwd":"123456"}
        try:
            res = HttpRequest(log_url,'post',log_data).http_request().json()
        except Exception as e:
            raise Exception("请求参数有误")
        else:  #断言
            self.assertIn('登录成功',res['msg'])
            self.assertIn('10001',res['code'])
        #不输入密码
        def test_02(self):
            log_data = {"mobilephone": "18688773467"
                        }
            try:
                res = HttpRequest(log_url, 'post', log_data).http_request().json()
            except Exception as e:
                raise Exception("请求参数有误")
            else:  # 断言
                self.assertIn('密码不能为空', res['msg'])
                self.assertIn('20103', res['code'])
        def test_03(self):
            log_data = {
                    "pwd":"123456"}
            try:
                res = HttpRequest(log_url, 'post', log_data).http_request().json()
            except Exception as e:
                raise Exception("请求参数有误")
            else:  # 断言
                self.assertIn('手机号不能为空', res['msg'])
                self.assertIn('20103', res['code'])
#密码输入错误
        def test_04(self):
            log_data = {"mobilephone":"18688773467",
                    "pwd":"hhhhhh123456"}
            try:
                res = HttpRequest(log_url, 'post', log_data).http_request().json()
            except Exception as e:
                raise Exception("请求参数有误")
            else:  # 断言
                self.assertIn('用户名或密码错误', res['msg'])
                self.assertIn('20111', res['code'])
class Recharge(unittest.TestCase):
    get_cookies = requests.post(log_url,data={"monilephone":"18688773467","pwd":"123456"},verify = False).cookies
     #正常充值
    def test_05(self):
        log_data = {'mobilephone':'18688773467','amount':'10000'}
        try:
            res = HttpRequest(recharge_url, 'post', log_data,cookies=Recharge.get_cookies).http_request().json()
        except Exception as e:
            raise Exception("请求参数有误")
# 断言
        else:
            self.assertIn('充值成功', res['msg'])
            self.assertIn('10001', res['code'])

    def test_06(self):
        log_data = {'amount':'10000'}
        try:
            res = HttpRequest(recharge_url, 'post', log_data,cookies=Recharge.get_cookies).http_request().json()
        except Exception as e:
            raise Exception("请求参数有误")
        else:  # 断言
            self.assertIn('手机号不能为空', res['msg'])
            self.assertIn('20103', res['code'])
#不输入金额
    def test_07(self):
         log_data = {'mobilephone':'18688773467'}
         try:
             res = HttpRequest(recharge_url, 'post', log_data,cookies=Recharge.get_cookies).http_request().json()
         except Exception as e:
             raise Exception("请求参数有误")
         else:  # 断言
             self.assertIn('请输入金额', res['msg'])
             self.assertIn('20115', res['code'])
#输入错误的金额
    def test_08(self):
        log_data = {'mobilephone': '18688773467','amount':'哈哈'}
        try:
            res = HttpRequest(recharge_url, 'post', log_data, cookies=Recharge.get_cookies).http_request().json()
        except Exception as e:
            raise Exception("请求参数有误")
        else:  # 断言
            self.assertIn('请输入金额', res['msg'])
            self.assertIn('20115', res['code'])

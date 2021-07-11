import requests

class HttpRequest:
    @staticmethod
    def http_request(url,data,method,cookie = None):
        try:
            if method.lower() == "get":
                res = requests.get(url,data,cookies = cookie)
            elif method.lower() == "post":
                res = requests.post(url,data,cookies = cookie)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise e
        return res  #返回消息实体


if __name__ == '__main__':
    #注册
    register_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    register_data = {"mobilephone":"15096098888","pwd":"12345","regname":"小小"}
    # register_res = requests.get(register_url,register_data)
    register_res = HttpRequest().http_request(register_url,register_data)
    print("注册结果是：{}".format(register_res.json()))

    #登录
    login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    login_data = {"mobilephone": "15096098888", "pwd": "123456"}
    login_res = HttpRequest().http_request(login_url, login_data, "post")
    print("登陆结果是：", login_res.json())

    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {"mobilephone": "15096098888", "amount": "2000"}
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, "get", login_res.cookies)
    print("充值结果是：", recharge_res.json())




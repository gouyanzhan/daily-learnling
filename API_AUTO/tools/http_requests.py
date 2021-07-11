import requests
class HttpRequest:
    '''利用requests封装get请求和post请求'''
    def http_request(self,url,data,method,cookie=None):
        # url：请求地址  http：//xxx：port,
        # param：传递的参数  非必填参数  字典的格式传递参数
        # method: 请求方式 支持get 以及post  字符串你形式的参数
        # cookie: 请求的时候传递的cookie值
        if method.lower() == "get":
            res = requests.get(url, data, cookies=cookie)
        else:
            res = requests.post(url, data, cookies=cookie)  # 响应结果的消息实体
        return res # 返回一个消息实体


if __name__ == '__main__':
    url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    data = {"mobilephone": "1310000000", "pwd": "123456"}
    res = HttpRequest().http_request(url,data,"post")
    print("登陆结果是：",res.json())

#充值
    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {"mobilephone":"18688773467","amount":"2000"}
    recharge_res = HttpRequest().http_request(recharge_url,recharge_data,"get",res.cookies)
    print("充值结果是：",recharge_res.json())

# https requests.get(url,data,verify = False)



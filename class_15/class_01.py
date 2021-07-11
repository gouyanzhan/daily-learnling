import requests
class HttpRequest:
    def __init__(self):
        self.url = url;
        self.data = data;

    def get_request(self):
        res = requests.get(self.url,self.data)
        print("返回的结果是{0}".format(res))

    def post_request(self):   #实例方法只能通过实例来调用
        res = requests.post(self.url,self.data)
        print("返回的结果是{0}".format(res))

    @classmethod
    def add(cls):
        print("我是类方法")
        return 10

    @staticmethod
    def print_msg():
        print("我是静态方法")

#类方法  静态方法  ---- > 可以直接类名.方法名调用    也可以通过实例调用

HttpRequest.add()
HttpRequest.print_msg()
HttpRequest(1,2).print_msg()

# 实例方法必须要创建实例来调用  类名()
url = "http://www.baidu.com"
data = {'mobilephone':'13100000000','pwd':'123456'}
HttpRequest().get_request(url,data)


#类方法  静态方法 ---》不能调用类的属性值
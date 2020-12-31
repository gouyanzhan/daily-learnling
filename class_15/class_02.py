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



#重写 ： 跟父类的函数名重复了 就叫重写
#拓展： 函数名是父类里面没有的 就叫拓展
class  PythonHttpRequest(HttpRequest):  #继承


    def __init__(self,a,b,url,data):
        super(PythonHttpRequest, self).__init__(url,data)   #超继承  调用父类里面的__init__方法
        self.a = a
        self.b = b

    def print_msg(self):
        self.get_request()  #类里面的方法  属性 只能是实例调用
        print("我是一个没用的函数，我在这里要调用父类的函数")

    def add(self):
        print("a+b=",self.a+self.b)


#继承的时候  子类要不要传初始化参数 看父类

url ='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
data = {'mobilephone':'18688773467','pwd':'123456'}
a = 1
b = 2

PythonHttpRequest(url,data).print_msg()
PythonHttpRequest(url,data).get_request()

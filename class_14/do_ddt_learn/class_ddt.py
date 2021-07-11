#ddt  ddt+unittest  来进行数据的处理  第三方库

# 装饰器  可以自行去了解  会在你的函数运行之前运行
import unittest

from ddt import ddt,data,unpack
# test_data = [[1,3],[4,5]]
#列表里面嵌套字典
test_data= [{"no":1,"name":"haha"},{"no":2,"name":"xixi"}]
@ddt #装饰测试类
class TestMath(unittest.TestCase):
    @data(*test_data)   #装饰测试方法 拿到几个数据，就执行几条用例，*：脱外套
    # def test_print_data(self,item): #测试用例
    #     print("item:",item)
    @unpack  #针对每一条数据，根据逗号拆分
    #如果unpack后的参数 少于5个  推荐用unpack
    #要注意参数不对等的情况，提供对应个数的参数来接收变量
    #如果要对字典进行unpack的话  参数名与你的字典key对应
    # 法一：
    def test_print_data(self, no,name):  # 测试用例
        print("no:", no)
        print("name:",name)
     #法二：不用unpack
    def test_print_data(self,a): #测试用例
        print("no:",a["no"])
        print("name:",a["name"])


    # def test_add(self):
    #     a = 10
    #     b = 20
    #     print(a + b)
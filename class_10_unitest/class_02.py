
# 这个类的实例是一个个的单独用例
# instance   单数 实例
# instances  复数 实例们
# 创建实例
import unittest
import HTMLTestRunnerNew  #写好的一个模块，可以直接调用
from class_10_unitest.class_01 import TestMathMethod  #具体到类名

suite = unittest.TestSuite()    #存储用例

#方法一：
#只执行一条  两个正数相加
# suite.addTest(TestMathMethod('test_add_two_positive'))
# suite.addTest(TestMathMethod('test_add_two_zero'))
# #执行
# runner = unittest.TextTestRunner()
# runner.run(suite)


#方法二：TestLoader

loader = unittest.TestLoader()  #创建一个加载器
#从测试类里面去找
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
#从模块里面去找
from class_10_unitest import class_01  #具体到模块
suite.addTest(loader.loadTestsFromModule(class_01))

#执行
# file = open("test.txt","w+",encoding="UTF-8")   #没有关闭文件
with open("test.txt","w+",encoding="UTF-8") as file:  #上下文管理器,可以用完就关闭文件
    runner = unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suite)
print(file.closed)

#新鲜 html
with open("test_report.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="python11期单元测试报告",
                                              description="描述",
                                              tester = "jessica")
    runner.run(suite)
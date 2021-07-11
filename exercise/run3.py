import unittest
import HTMLTestRunnerNew
from exercise.tools.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
suite.addTest(TestHttpRequest('test_api')) # 测试类的实例

with open("test_result/html_report/test_api.html","wb") as file:


    #执行用例
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream = file,verbosity = 2,title = "单元测试报告",descripyion = "单元测试报告",tester = "gyz")
    runner.run(suite)
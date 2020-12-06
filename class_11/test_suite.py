import unittest
import HTMLTestRunnerNew
from class_11 import test_http   #模块名


suite = unittest.TestSuite()

# 通过loder方式加载用例
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromModule(test_http))

#执行
with open("test_summer.html") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester = None)
    runner.run(suite)


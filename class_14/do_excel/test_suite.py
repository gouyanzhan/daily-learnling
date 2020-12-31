import unittest
import HTMLTestRunnerNew
from class_14.do_excel.test_http import TestHttp   #类名
from class_14.do_excel.do_excel import DoExcel


# test_data = DoExcel("test3.xlsx","python").get_data()

# ddt  loader
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))
# for item in test_data:  #创建实例
#     # suite.addTest(TestHttp("test_api",test_data[0]["url"],test_data[1]["data"],
#     #                           test_data[2]["method"],test_data[3]["expected"]))#实例的方式去加载用例 url,data,method,expected
#     suite.addTest(TestHttp("test_api", item["url"], eval(item["data"]),item["method"], str(item["expected"])))


#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester = None)
    runner.run(suite)


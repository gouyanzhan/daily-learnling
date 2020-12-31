import unittest
import HTMLTestRunnerNew
from class_13.test_http import TestHttp   #类名
from class_13.do_excel_3 import DoExcel

t = DoExcel("test3.xlsx","python")

suite = unittest.TestSuite()
for i in range(1,t.max_row + 1):
    suite.addTest(TestHttp("test_api", t.get_data(i ,1),t.get_data(i,2),eval(t.get_data(i,3)),str(t.get_data(i,4))))


#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester = None)
    runner.run(suite)
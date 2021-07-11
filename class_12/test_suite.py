import unittest
import HTMLTestRunnerNew
from class_12.test_http import TestHttp   #类名

test_data = [{"url":"http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data":{"mobilephone": "1310000000", "pwd": "123456"},"expected":"10001","method":"get"},
             {"url":"http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data":{"mobilephone": "1310000000", "pwd": "123456789"},"expected":"20111","method":"post"},
             {"url":"http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data":{"mobilephone": "1310000000", "amount": "1000"},"expected":"10001","method":"get"},
             {"url":"http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data":{"mobilephone": "1310000000", "amount": "-1000"},"expected":"20117","method":"post"}]

suite = unittest.TestSuite()
for item in test_data:  #创建实例
    # suite.addTest(TestHttp("test_api",test_data[0]["url"],test_data[1]["data"],
    #                           test_data[2]["method"],test_data[3]["expected"]))#实例的方式去加载用例 url,data,method,expected
    suite.addTest(TestHttp("test_api", item["url"], item["data"],item["method"], item["expected"]))


#执行
with open("test_summer.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title=None,description=None,tester = None)
    runner.run(suite)


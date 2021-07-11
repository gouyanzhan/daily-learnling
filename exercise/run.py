from exercise.tools.http_request import HttpRequest
from exercise.tools.da_excel import DoExcel

COOKIE = None

def run(test_data,sheet_name):  #列表嵌套字典的数据格式进来
    global COOKIE
    for item in test_data:
        print("正在测试的用例是{0}".format(item["title"]))
        res = HttpRequest().http_request(item["url"],eval(item["data"]),item["http_method"],COOKIE)
        if res.cookies:
            COOKIE = res.cookies
        print("请求的结果是：{0}".format(res.json()))
        DoExcel().write_back("test_data/test_data.xlsx",sheet_name,item['case_id']+1,str(res.json()))

test_data = DoExcel().get_data("test_data/test_data.xlsx","recharge")
run(test_data,'recharge')

# test_data = [{"login_url": 'http://119.23.241.154:8080/futureloan/mvc/api/member/login',
#               "login_data": {"mobilephone": "15096098888", "pwd": "123456"}, "title": "正常登录","http_methd":"get"},
#              {"login_url": 'http://119.23.241.154:8080/futureloan/mvc/api/member/login',
#               "login_data": {"mobilephone": "15096098888", "pwd": "123456789"}, "title": "异常登录","http_method":"post"}]
#
#
# run(test_data)
    #登录
    # login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    # login_data = {"mobilephone": "15096098888", "pwd": "123456"}

    #充值
    # recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    # recharge_data = {"mobilephone": "15096098888", "amount": "2000"}
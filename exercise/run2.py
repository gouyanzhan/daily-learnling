from exercise.tools.get_cookie import GetCookie
from exercise.tools.http_request import HttpRequest
from exercise.tools.da_excel import DoExcel

# COOKIE = None

def run(test_data,sheet_name):  #列表嵌套字典的数据格式进来
    # global COOKIE
    for item in test_data:
        print("正在测试的用例是{0}".format(item["title"]))
        res = HttpRequest().http_request(item["url"],eval(item["data"]),item["http_method"],getattr(GetCookie,'Cookie'))
        if res.cookies:
            # COOKIE = res.cookies
            setattr(GetCookie,'Cookie',res.cookies)
        print("请求的结果是：{0}".format(res.json()))
        DoExcel().write_back("test_data/test_data.xlsx",sheet_name,item['case_id']+1,str(res.json()))

test_data = DoExcel().get_data("test_data/test_data.xlsx","recharge")
run(test_data,'recharge')
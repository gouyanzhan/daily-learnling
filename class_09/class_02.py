#requesrs   第三方库

import requests
#get请求

url = 'http://120.78.128.25:8765/Index/login.html'
res = requests.get(url)   #返回一个消息实体
print(res.headers)
print(res.status_code)
print(res.text)  #html
print(res.json())  #会报错

#post 请求   带参数
url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
data = {"mobilephone":"1310000000","pwd":"123456"}
res = requests.post(url,data)
print("响应头：",res.headers)
print("响应状态码：",res.status_code)
print("cookies",res.cookies)   #类字典形式key取值
print("响应正文1",res.text)  #str    json
print("响应正文2",res.json())  #不会报错 dict  json
# html  xml  json ---》 text
# html  xml ---》 json()会报错，只有json类型的返回值才支持json

#充值
recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
recharge_data = {"mobilephone":"18688773467","amount":"2000"}
recharge_res = requests.get(recharge_url,recharge_data,cookies = res.cookies)
print("充值结果:",recharge_res.json())
print("状态码:",recharge_res.status_code)


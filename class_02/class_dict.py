#字典  dict  符号{}  无序
# 1:可以存在空字典a =[]
# 2:字典里面数据存储的方式 key:value
# 3：字典里面的元素  根据逗号来进行分隔
# 4: 字典里面value可以包含任何类型的数据


a = {}
print(type(a))
a = {"class":"python11",
     "student":119,
     "teacher":"girl",
     "t_age":20,
     "score":[99,88,100,5]}

#字典取值： 字典[key]
print(a["score"])

#删除 pop(key)
res = a.pop("teacher")
print(res)

#新增值 a[新key]=value  字典里面不存在的key
a["name"] = "华华"
print(a)

#修改 a[已存在的key] =新value   字典里面不存在的key
a["name"] = "华华"
print(a)




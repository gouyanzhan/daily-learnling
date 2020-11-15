#控制语句  分支分流  循环语句  for  while

#判断语句  id  elif  else  关键字
# if （比较/逻辑/成员运算符 均可） 空数据 = false  非空数据= true
age = 20
if age>18:
    print("恭喜你，成年了！")
s = "3"
if s:
    print("hhh")

#if 条件语句
#   子语句
#else：
#   子语句
age = 20
if age > 19:
    print("恭喜你，成年了！")
else:
    print("哼")

#if  elif
age = 20
if age > 19:
    print("恭喜你，成年了！")
elif 18 > age >0:
    print("哼")
else:
    print("hhh")

#input（）函数  从控制台获取一个数据 获取的数据都是字符串类型
age = int(input("请输入："))



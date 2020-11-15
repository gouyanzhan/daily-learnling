#一家商场在降价促销，如果购买金额50-100元（包含50和100）之间，会给10%折扣
#如果购买金额大于100元，会给20%折扣
#编写一个程序，询问购买价格，再显示出折扣（%10或20%）和最终价格

# a = int(input("请输入购买金额"))
# if a>=50 and a<=100:
#     print( a * 0.9)
# elif a > 100:
#     print( a * 0.8)
# else:
#     print(a)

#生成随机整数，从1-9取出来
#然后输入一个数字，来猜，如果大于，则打印bigger
#小了则打印less
#如果相等，则打印equal
# import random
# a = random.randint(1,9)
# b = int(input("请输入一个0-9的数字"))
# print("随机数是{}".format(a))
# if b > a:
#     print("bigger")
# elif b < a:
#     print("less")
# else:
#     print("equal")


# 一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入
#编写一个程序，询问用户的性别（m表示男性  f表示女性）和年龄
#然后显示一条消息指出这个人是否可以加入球队，询问10次后
#输出满足条件的总人数
# sum = 0
# for item in [1,2,3,4,5,6,7,8,9,10]:
#     sex = input("请输入性别（f/m）:")
#     if sex == "m":
#         print("您不符合要求")
#     elif sex == "f":
#         age = (int(input("请输入年龄:")))
#         if age >= 10 and age <= 12:
#             print("您可以加入球队")
#             sum = sum + 1
#         else:
#             print("您不可以加入球队")
# print(sum)
# #法二
# i = 10 #记录询问次数
# count = 0 #记录符合条件的人数
# while True:
#     sex = input("请输入你的性别：")
#     if  sex == "f":
#         age = int(input("请输入你的年龄："))
#         if 10<=age <= 12:
#             print("bingo")
#             count += 1
#             i-=1
#         else:
#             print("sorry")
#             i -= 1
#     else:
#         print("sorry")
#         i -= 1
#     if i == 0:
#         break #结束循环 跳出循环
#     else:
#         continue  #结束本轮循环，继续下一轮

#输入num为四位数，对其按照如下的规则进行加密：
#1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
#2）将该数的第一位和第四位互换，第二位和第三位互换
#3）最后合起来作为加密后的整数输出
#优酷笔试题
try:
    num = input("请输入一个四位数：")
    new_num = ""
    if len(num) == 4:
        for item in num:
            new_num += str((int(item) + 5) % 10)
        last_num = new_num[::-1]
        print("加密后的整数为{0}".format(last_num))
    else:
        print("您输入的不是四位整数！")
except Exception:
    print("您输入的四位数有误！")






#例如：passwd= {"admin":"123321","user1":"123456"}
#1.设计一个登陆程序，不同的用户名和对应密码存在一个字典里面，输入正确的用户和密码去登陆
#2.首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
#3.当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误，请重新输入
#4.如果密码输入错误超过三次，中断程序运行
#5.当输入密码错误时，提示还有几次机会
#6.用户名和密码都输入成功时，提示登陆成功！

passwd = {"admin":"123321","user1":"123456"}
count = 3
while True:
    username = input("请输入用户名：")
    if username in passwd.keys():

        while count > 0:
            password = input("请输入密码：")
            if password == passwd[username]:
                print("登陆成功！")
                break
            else:
                print("密码错误，请重新输入")
                count -=1  #每次密码错误的时候  减去1
                print("你还有输入密码的{0}次机会".format(count))
        break
    elif username not in passwd.keys() or username == "":
        print("请输入正确的用户名")

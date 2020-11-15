#一个班级有一个花名册，存在列表里面
#你从控制台输入一个名字，如果这个名字在花名册里面，
#就打印这个用户名正确  如果不存在，那就报错

# name = ["huahua","ta","tingting","kaka"]
#
# username = input("请输入你的名字：")
# if username in name:
#     print("bingo")
# else:
#     print("sorry")

#while  控制循环
#语法：
#while 条件表达式   #逻辑 成员 比较 空数据(参照if语句) 布尔值
    #代码块

#执行规律：首先判断while后面的条件表达式是否成立
#如果是True 那就执行代码块  否则不进入代码块，执行完毕之后，继续判断--->如果true，那就执行代码块，执行完毕之后
#否则 不进入内部执行代码块
# while True:
#     print("要结束循环是不可能的！")
# #防止代码进入死循环，加一个变量来控制循环次数
# a = 1
# while a<=10:
#     print("hhh")
#     a = a + 1

#利用while循环 实现1-100的整数相加
a = 0
sum = 0
while a <=100:
    sum = sum + a
    a = a + 1
print(sum)

# while 与if 语句搭配使用  break  continue
# 一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入
#编写一个程序，询问用户的性别（m表示男性  f表示女性）和年龄
#然后显示一条消息指出这个人是否可以加入球队，询问10次后
#输出满足条件的总人数

i = 10 #记录询问次数
count = 0 #记录符合条件的人数
while True:
    sex = input("请输入你的性别：")
    if  sex == "f":
        age = int(input("请输入你的年龄："))
        if 10<=age <= 12:
            print("bingo")
            count += 1
            i-=1
        else:
            print("sorry")
            i -= 1
    else:
        print("sorry")
        i -= 1
    if i == 0:
        break #结束循环 跳出循环
    else:
        continue  #结束本轮循环，继续下一轮









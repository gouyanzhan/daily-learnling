# for i in range(1,6):#控制行数 1，2，3，4，5
#     for j in range(1,i+1):
#         print("*",end="")
#     print("") #print语句换行
    # *  i= 1 j =1
    # **  i=2 j=2
    # ***
    # ****
    # *****  i=5 j=5

#2:等边三角形  每个边都是5个星号

# for i in range(1,6):
#     # print("这个是第{0}行".format(i))
#     # print("*")
#     #一个for循环控制 空格的输出
#     #一个gor循环控制"*"的输出
#     for j in range(1,6-i):
#         print(" ",end="")
#
#     for k in range(1,i+1):
#         print("*  ",end="")
#     print("")


#3:输出一个99乘法表

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("{0}*{1}={2} ".format(j,i,j*i),end="")
#     print("")

#4:经典冒泡算法： 利用for循环 完成a = [1,7,4,89,34,2]的冒泡排序
#冒泡排序：小的移前面 大的排后面
#排序，最终使得数组中的这几个数字按照从小到大的顺序排序
#冒泡的概念 关系到接下来怎么写程序
#相邻的两个元素 依次比较

# a = [1,7,4,89,34,2]  #冒泡算法  一般最多比较n-1次就完成
# # for i in range(1,len(a)):
# #     for j in range(0,len(a)-1):
# #         if a[j] > a[j+1]:
# #             a[j],a[j+1] = a[j+1],a[j]
# #     print(a)
# # print(a)

#5:写函数，将姓名，性别，城市作为参数，并且性别默认为f（女），如果城市是长沙并且性别为女，则输出姓名，性别，
#城市，并返回True，否则返回False

def param(name,city,sex = "f"):
    if city == "长沙" and sex == "f":
        print(name,sex,city)
        return True
    else:
        return False


#6： 定义一个函数，成绩作为参数传入，如果成绩小于60，则输出不及格，如果成绩在60到80之间，
#则输出良好，如果成绩高于80分，则输出优秀，如果成绩不在0-100之间，则输出成绩输入的错误

def score(a):
    if a < 60:
        print("成绩不及格")
    elif 60 <= a <= 80:
        print("良好")
    elif 80 < a <= 100 :
        print("优秀")
    else:
        print("成绩输入错误")
score(100)


#7:自动贩卖机：只接收1元、5元、10元的纸币或硬币
#可以1块，5元，10元，最多不超过10元，
# 饮料有橙汁，椰汁，矿泉水，早餐奶，售价分别是3.5,4,2,4.5
#写一个函数用来表示贩卖机的功能，用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零

#思路：
#选择饮料
#投钱
#判断：1：钱不够 2：钱多了 3：钱刚好
def auto_buy():
    drinks = {"1":3.5,"2":4,"3":2,"4":4.5}
    #用户选择饮料
    total = 0
    while True:
        choose = input("请选择要购买的饮料：")
        if choose in drinks.keys():
            total += drinks[choose]
        elif choose == "q":
            print("退出选择饮料")
            break
        else:
            print("不存在，请重新选择")

    #用户投币
    toubi = 0 #投币总额
    while True:
        money = input("请投币")
        if money == "1" or money == "5" or money == "10":
            toubi += money
            if toubi > total:
                print("您刚购买了{0}元饮料，您已支付{1}元，找零{2}".format(total, toubi,toubi - total))
                break
            elif toubi < total:
                print("您刚购买了{0}元饮料，您已支付{1}元，还需支付{2}".format(total, toubi, total - toubi))
            else:
                print("您刚购买了{0}元饮料，您已支付{1}元，已支付完毕！".format(total, toubi))
                break
        elif money == "q":
            print("退出投币")
            break
        else:
            print("您输入的选项不存在")
auto_buy()











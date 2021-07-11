#循环 for  for循环语法：
# for  item  in  某个数据类型：（数据类型包含：字符串  列表  元组 字典  集合等）
     #代码块

#in？ 成员运算符  in
# for 循环的循环次数  由数据的元素个数决定
# s = 'hello'
# l =[1,2,3]
# d ={"age":18,"name":"哈哈"}   #字典类型的数据  是遍历访问key
# for item in s:   #for循环遍历s里面的元素  然后赋值给item
#     print("hhh")
# for a in s:
#     print(a)

#题目
#请利用for循环，完成列表里面的所有数据的相加
L = [5,6,9,3,7]
sum = 0  #存储和
for i in L:
    sum = sum + i
print(sum)


d ={"age":18,"name":"哈哈"}
print(d.values())  #获取字典里面的所有value值
print(d.keys())    #获取字典里面的所有key值
# for item in d:
#     print(d[item])

for item in d.values():
    print(item)


#range 函数  range(m,n,k) m头 n尾  k步长 默认为1，取头不取尾
range(1,5,1) #1，2，3，4
range(1,6,2)  #1 3 5
range(8) #头默认为0 ，1 2 3 4 5 6 7

for item in range(3):
    print("循环次数")

L= [5,6,9,3,7]
#请利用for循环  根据L的索引值，打印出列表中每个元素的值
# 0 1 2 3 4  range(5)
for i in range(5):
    print(L[i])

#请利用for循环和range函数  完成1-100整数相加和（包含1，100）
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)


#嵌套循环 请把列表里面的每一个元素单独打印出来
L = [["monica","生生","小黄","gugu"],["halen","hah","hhh"]]
for item in  L:    #每循环一次，拿到一个子列表
    for a in item:
        print(a)


#利用嵌套for循环生产一个直角三角形图形
# *
# **
# ***
# ****
# *****
for a  in range(1,6):
    print("*"* a)






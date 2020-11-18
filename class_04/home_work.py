#输入num为四位数，对其按照如下的规则进行加密：
#1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
#2）将该数的第一位和第四位互换，第二位和第三位互换
#3）最后合起来作为加密后的整数输出

num = input("请输入4位数：")
new_num = ""
for item in num:
    print(item)
    print("每位加5然后摸10",(int(item) + 5)%10)
    new_num += str((int(item)+5)%10)
last_str = print(new_num[::-1])
print(last_str)


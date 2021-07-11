#return
# def numbers(m,n,k):    #默认参数必须放在位置参数之后
#     sum = 0
#     for i in range(m,n,k):
#         sum  =sum + i
#     return sum
#
# numbers(1,10,2)
# print(numbers(1,10,2))

#return  在函数里面相当于一个结束符号  表示函数到此为止！！！！
#后面的代码不会被执行
# def add_two(a,b):
#     return (a+b)
#     print("！！")
#
# print(add_two(1,3)+10)

#6，写函数，检查传入列表的长度，如果大于2
#那么仅仅保留前两个长度的内容，并将新内容返回

def check_list(L):    #形参
    if len(L) > 2:
        new_list = L[0:2]
    return new_list
L = [1,2,3,4]       #实参
new_list = check_list(L)
print(new_list)


#动态参数/不定长参数  *args  arguments
#在函数内部 作为元组来传递
# def make_sandwich(a,b,c,d):
#     print("您的三明治包含了{0}、{1}、{2}、{3}".format(a,b,c,d))
# make_sandwich('生菜','鸡蛋','培根','牛肉')
#
# def make_sandwich(*args):
#     print(args)
# make_sandwich('生菜','鸡蛋','培根','牛肉')

# def make_sandwich(*args):
#     all = ""
#     for item in args:
#         all += item
#         all += "、"
#     print("您的三明治包含了" + all)
# make_sandwich('生菜','鸡蛋','培根','牛肉')
# make_sandwich()

#关键字参数  key-value  **kwargs  key word
#在函数里面体现为 字典
def kw_function(**kwargs):
    print(kwargs)

kw_function(x=1,y=2)

def add_all_num(*L,a):
    print(L)#元组
    sum = 0
    for item in L:
        sum += item
    print("和为",sum)
    print("a的值",a)

    add_all_num(1,2,3,4,5,6,a=7)

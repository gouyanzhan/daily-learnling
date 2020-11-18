# python的内置函数
#试错
#print input  len  type  str  float  list  range
#pop append  insert  keys  split  replace  strip
# remove  clear

#总结一下函数的特点：
#可以重复使用

#函数的语法： def  关键字
#def 函数名():
    #函数体 ：你希望这个函数去给你实现什么功能？
#调用： 函数名()

def da_lao(name):   #形参/位置参数  2）默认参数  def da_lao(name = "hhh")
    print("{0}是大佬".format(name))

#调用函数
da_lao("hhh")  #实参

#请把1-100的连续整数相加功能  写成一个函数

def numbers(m,n,k=2):    #默认参数必须放在位置参数之后
    sum = 0
    for i in range(m,n,k):
        sum  =sum + i
    print(sum)
numbers(1,10,2)

#第一步：先用代码实现功能，还可以选取一组数据来证明自己的diamante是否正确
#第二步：先变成函数 加def
#第三步：想办法提高代码的复用性


# 字符串的 translate
#swapcase





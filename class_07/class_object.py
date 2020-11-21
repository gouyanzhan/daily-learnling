#类的划分标准，写代码的人来定
#python 类的语法   关键字class   def  函数名（参数）：函数的关键字
#class  类名：#类名的规范  数字字母下划线组成  不能以数字开头  首字母大写  驼峰命名
# 类属性
# 类方法

class BoyFriend:
    #类属性
    height = 175
    weight = 130
    money = "500万"
    #类函数/类方法
    def cooking(self): #会做饭
        print("男朋友要会做法")
    def earn(self): #会赚钱
        print("男朋友月薪3万")
    def print_msg(self):     #self为固定的占坑符号  类里面的方法必须带self这个参数
        print(self)

#实例/对象  具体一个例子 类名（）
bf = BoyFriend()  #bf 是一个实例
print(bf)

print(bf.money)
print(bf.cooking())
bf .print_msg()

#实例具有类里面的所有属性和方法的使用权限
#调用属性  实例.属性名
#调用方法/函数  实例.方法名（）  实例.函数名（）



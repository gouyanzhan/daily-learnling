# 列表 list  符号[]
a = [1,0.02,'hello',[1,2,3],True]

# 1:可以存在空列表a =[]
# 2:列表里面可以包含任何类型的数据
# 3：列表里面的元素  根据逗号来进行分隔
# 4：列表里面的元素 也是有索引  索引值从0
# 5： 获取列表里面的单个值：列表[索引值]
print(a[2])
print(len(a))
# 6:列表的切片 同字符串的操作  列表名[索引头：索引尾 ：步长]

print(a[::2])
print(a[0:5:2])   # 0 2 4

# 什么时候才会用列表？
# 列表用例存储数据
# 如果你要存储的数据是一个类型的，建议用列表
# 如何往列表里面增加数据    可以添加任何类型的数据

#append   追加在末尾  每次只能添加一个
a.append("秦天")
print("a列表的值{0}".format(a))

# insert 插入数据  想放哪就放哪 但是要指定位置
a.insert(2,"monica")
print(a)

#删除 pop()
a.pop()   #默认删除最后一个元素
a.remove(1)  #指定删除某个值

a.pop(2)  #  传入索引值   删除指定索引位置的元素

res = a.pop()   #pop函数   会返回被删除的那个元素   函数return关键字
print("a的列表值{0}".format(res))

#修改  a[索引值]= 新值
a = [1,0.02,'hello',[1,2,3],True]
a[2] = '初心'  #赋值运算
print("a列表的值{0}".format(a))


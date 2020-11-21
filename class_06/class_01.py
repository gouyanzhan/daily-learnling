import os

#新建一个目录/新建一个文件夹
# os.mkdir("Alisa")

#跨级新建目录  用/符号代表路径的不同层级
# 必须确保上面的层级是存在的
# os.mkdir("Alisa/vict")
#
# os.mkdir("D:\\test_python11")

#转义字符 \n  \r   我们可以通过加\ 还有r R 来让转义字符失效

#删除   删除文件  也是一级一级的删除
#拓展一：  python可否强制删除
# os.mkdir("Alisa/vict")
# os.rmdir("Alisa")   #报错：OSError: [Errno 66] Directory not empty: 'Alisa'

#拓展二：怎么新建文件 open  删除文件？

#路径的获取1
path_1 = os.getcwd()     #获取当前工作的目录   具体到最后一级目录
print("获取到当前路径是：{0}".format(path_1))

#路径的获取2    #获取当前文件所在的绝对路径     具体到 模块名
path_2 = os.path.realpath(__file__)
print("获取到当前路径是：{0}".format(path_2))

#第三个知识点：如何拼接路径
# new_path_1= os.getcwd() + "/python1"
# print(new_path_1)
# os.mkdir(new_path_1)

#join
# new_path_2 = os.path.join(os.getcwd(),"python666","sub_1")
# print(new_path_2)
# os.mkdir(new_path_2)
#判断是文件还是目录
# print(os.path.isfile(__file__))   #返回值 布尔值
# print(os.path.isdir(os.getcwd()))

#怎么判断文件是否存在？
print(os.path.exists("/Users/gouyanzhan/PycharmProjects/python11/class_06"))

#罗列当前路径的所有文件和目录
print(os.listdir(os.getcwd()))

#拓展题：
#给的一个路径，请打印出所有路径（直至这个路径下没有目录为止）
#思路：递归函数  写成一个函数
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(),path))
        print("{0}还需要做下一步处理".format(path))
    else:
        print("已穷尽" ,os.path.join(os.getcwd(),path))







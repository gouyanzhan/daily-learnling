#异常处理&调试
#异常：运行代码过程中遇到的任何错误 带有error
#异常处理：我们对代码中所有可能会出现的异常 进行的处理
#疑问：为什么要去进行处理？

import os
try: #警察
    os.mkdir("Alisa")   #FileExistsError    #嫌疑人
except FileExistsError:
    print("抓捕归案，等待进一步处理")
print("我就是这么厉害，哈哈！")

#1：处理某个错误  2：处理某种类型的错误  #3：有错就抓
# try: #警察
#     os.mkdir("Alisa")   #FileExistsError    #嫌疑人
# except : #except 警力出动
#     print("抓捕归案，等待进一步处理")
#既要抓 还要有处罚措施
try:
    os.rmdir("Alisa") #OSError
except Exception as e:   # 把错误抓起来，存到变量e里面去 error
    print("抓捕归案，等待进一步处理")
    print("错误为：{0}".format(e))
    #拿一个小本本记起来
    file = open("error.txt","a+",encoding='UTF-8')
    file.write(str(e))
    file.close()  #关闭文件

#2:try...except...finally
try:
    os.rmdir("Alisa") #OSError
except Exception as e:   # 把错误抓起来，存到变量e里面去 error
    print("抓捕归案，等待进一步处理")
    print("错误为：{0}".format(e))
    #拿一个小本本记起来
    file = open("error.txt","a+",encoding='UTF-8')
    file.write(str(e))
    file.close()  #关闭文件
finally:   #我就是第一，你犯不犯错，我都要执行
    print("上面报错，不影响我")

#3：try...except ...else    #不常用
try:
    os.rmdir("Alisa") #OSError
except Exception as e:   # 把错误抓起来，存到变量e里面去 error
    print("抓捕归案，等待进一步处理")
    print("错误为：{0}".format(e))
    #拿一个小本本记起来
    file = open("error.txt","a+",encoding='UTF-8')
    file.write(str(e))
    file.close()  #关闭文件
else: #跟try下面的代码是一起的  你好我就好  你不好我就不好
    print("哈哈哈")

#os.rmkdir("Alisa")  #osError > FileExistsError  (错误也有层级)

# print(a)   #NameError: name 'a' is not defined

# def add(a,b):
#     print(a+b)
# add(3)       #TypeError: add() missing 1 required positional argument: 'b'

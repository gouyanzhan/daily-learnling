#file txt  xml  html --->
file = open("python11.txt","r+",encoding='utf-8')
#mode 打开这个文件的模式
# r w a
# r+ w+ a+
#read write
# rb rb+   wb wb+   ab  ab+  #做单元测试了解
res = file.read()  #进行完一次读取操作之后，光标就到文末
file.write("卡卡")
print(res)

#1：file文件open之后默认是r  只读模式  如果你要写入内容,报错io.UnsupportedOperation: not writable
#2：r+  可读可写  先写的话  从头开始覆盖写  读光标之后的内容  读写跟着光标走
#3：如果要写入中文 要注意编码格式
#4：只写  硬要去读  就会报错
#5：w+ 可读可写  不管是w 还是w+，如果文件存在，直接清空，再重写
#如果文件不存在，新建一个文件，然后写
# file = open("python.txt","w")
# file.write("hhhhh")
#6: a  追加 a+
#如果文件存在  就直接追加写  写在后面  如果不存在 则新建一个文件进行结果写入
# file = open("python.txt","a",encoding='utf-8')
# file.write("\nyyyyy")    #\n 换行符

#重点掌握 r  a
file = open("python13.txt","r",encoding='utf-8')
print(file.read())

print(file.readline()) #按行读取 第一行
print(file.readline())  #第二行

print(file.readlines())  #读取多行  返回的是列表

file_2= open("python13.txt","a",encoding='utf-8')
print(file_2.write("20201119 file操作"))

file_3= open("python.txt","a",encoding='utf-8')
file_3.writelines(["777\n","888"])




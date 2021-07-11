#怎么去看函数
#怎么引入不同的模块--->
#第一步安装：
#a.在线安装  打开cmd
# 1） pip  install  模块名
# 2）pip  install 国内源地址 模块名
# 3）file-setting-project interpreter -->
#b.离线安装
#官网/百度找安装包
# 1.解压
# 2.拷贝解压后的文件到 python安装路径
# 3.命令到安装包文件路径 安装文件  setup.py
# 4.输入命令 python setup.py  install
a = [1,2,3,4]
print(a.pop())
#2.第三方库
#导入
#import
#from ...import...  至少具体到模块名

#测试代码
if __name__ == '__main__':    #主程序的执行入口，只有在当前模块下面执行的时候 才会执行
    pass
#反射

class GetData:
    Cookie = None
if __name__ == '__main__':

    print(GetData.Cookie)
    setattr(GetData,'Cookie',"小黄")  #可以直接把类里面的属性值做修改
    print(hasattr(GetData,"Cookie")) #判断是否有这个属性值
    print(getattr(GetData,"Cookie"))  #attribute 属性
    delattr(GetData,"Cookie") #删掉这个属性
    # print(GetData.Cookie)
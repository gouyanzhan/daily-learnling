#超继承
class MathMrthod:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("我是父类的加法" , self.a + self.b)
    def sub(self):
        return self.a - self.b

class MathMrthod_1(MathMrthod):
    def divide(self):     #拓展
        return self.a/self.b

    def add(self):     #重写
        super(MathMrthod_1, self).add()  # 超继承
        print("我是子类的加法" , self.a + self.b + 10)

MathMrthod_1(5,6).add()



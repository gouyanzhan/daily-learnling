class Teacher:
    def __init__(self,name,age=23):     #初始化函数  实例方法，一般不传动态参数和关键字参数
        self.name = name
        self.age = age
        self.height = 180
    def play_game(self,game_name):
        return (self.name + "会玩{0}".format(game_name))
    def coding(self,lines,language = "python"):   #self表示实例方法
        print(self.name + "会敲{0}代码，写了{1}行代码".format(language,lines))  #language 位置参数
    def cooking(self,*args):  #实例方法
        for item in args:
            print(self.name + "会做{0}".format(item))
    def teacher_info(self,*args):
        # self.cooking("海鲜大餐","蛋炒饭")
        self.cooking(*args) #参数不是写死的
        print("{0}老师，今年{1}岁，身高{2},可以嫁人了".format(self.name,self.age,self.height))
    @classmethod
    def swimming(cls):
        print("老师还有会游泳")
    @staticmethod
    def sing(name):
        print("要会唱{0}歌表演给学生看".format(name))

#初始化函数
t1 = Teacher("huahua","23")
t2 = Teacher("huhu","18")
t3 = Teacher("ddd","20")
t1.swimming()
t2.cooking("蛋炒饭","泡面")
t3.coding(1000)
print(t1.play_game("王者荣耀"))
t1.sing("有点甜")
#什么时候用初始化函数呢？
#想用就用
#如果某个属性值是多个函数共用的，就可以用初始化函数
t4 = Teacher("毛毛")
t4.teacher_info()
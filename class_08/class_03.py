#继承
class RobotOne:
    def __init__(self,year,name):
        self.year = year
        self.name = name
    def walking_on_ground(self):
        print(self.name + "只能在平地上行走")

    def robot_info(self):
        print("{0}年产生的机器人{1},是中国研发的".format(self.year,self.name))

#继承
class RobotTwo(RobotOne):

    def walking_on_ground(self):       #子类里面的函数名和父类函数名重复的时候，就叫重写
        print(self.name + "可以在平地平稳地上行走")
    def walking_avoid_block(self):    #拓展
        #我想在子类的函数里面调用父类的一个函数
        self.robot_info()
        print(self.name + "可以避开障碍物")



#继承的类  是否要用到初始化函数  请看是否从父类里面继承了
#1：父类有的，继承后，我都可以直接拿来用
#2：父类有，子类也有重名的函数，那么子类的实例就优先调用子类的函数
#3：父类没有，子类
r2= RobotTwo("1990","小王")
r2.robot_info()
r2.walking_on_ground()
r2.walking_avoid_block()


class RobotThree(RobotTwo,RobotOne): #第三代机器人继承第一代和第二代
    def __init__(self,year,name):
        self.year = year
        self.name = name
    def jump(self):
        print(self.name + "可以单膝跳跃")
r3 = RobotThree("2000","大王")
r3.robot_info()
#多继承的子类具有两个父类的属性和方法，
# 如果两个父类具有同名方法的时候，子类调用函数就近原则，谁在前就继承谁的
# 初始化函数也包括在内（就近父类无，子类可以重写初始化函数）

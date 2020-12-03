# 创建一个名为user 的类，其中包含属性 first_name 和 last_name，
# 还有用户简介通常会存储的其他几个属性。
# 在类user中定义一个名为describe_user()的方法，它打印用户信息摘要，
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法

class user():
    def __init__(self,first_name,last_name,sex,age,height,weight):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
    def describe_user(self):
        print(self.last_name + self.first_name + "的信息摘要:{0},{1}".format(self.sex,self.age))
    def greet_user(self,greet):
        print(self.last_name + self.first_name  + "向您发出{0}".format(greet))

user1 = user("三","张","女","20","165","40")
user2 = user("李","四","男","18","165","40")
user3 = user("王","五","男","23","165","40")

user1.describe_user()
user2.greet_user("哈喽")

# 定义一个学生类
# 1：有下面的类属性：姓名，年龄，成绩（语文，数学，英语）
# [每课成绩的类型为整数]，均放在初始化函数里面
# 2：类方法：
# 获取学生的姓名：get_name() 返回类型：str
# 获取学生的年龄：get_age() 返回类型：int
# 返回3门科目中最高的分数，get_course() 返回类型：int
#写好类以后，可以定义2个同学测试下： zm = Student('zhangming',20,[69,88,100])
#


class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_name(self):
        return(self.name)
    def get_age(self):
        return(int(self.age))
#     def get_course(self):
#         return(int(max(self.grade)))
# student01 = Student("zhangming",25,[99,99,99])
# print(student01.get_course())

    #  如果成绩放在了字典里面 ,高阶函数  sorted
    def get_course2(self):
        a = sorted(source.values(), reverse=True)
        grade = str(a[0])
        return(int(grade))

source = {"语文": 118, "数学": 55, "英语": 122}
student01 = Student("zhangming", 25, source)
print(student01.get_course2())

# 按照以下要求定义一个游乐园门票类，并创建实例调用函数，
# 完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定)
# 1、平日票价100元；2、周末票价为平日票价120%
# 3、儿童半价

class Ticket:
    def __init__(self, price = 100):
        self.price = price

    # def price_workday(self):
    #     man_price = self.price
    #     child_price = int(self.price * 0.5)
    #     return man_price,child_price
    #
    # def price_weekday(self):
    #     man_price = int(self.price * 1.2)
    #     child_price = int(self.price * 0.5 * 1.2)
    #     return man_price,child_price

    def calculate_cost(self):
        day = int(input("您需要购买哪天的票（1-5代表工作日，6-7代表周末）"))
        man =input("请输入您需要购买的大人人数的票")
        child =input("请输入您需要购买的儿童人数的票")
        if day  in range(1,6):
            total = int(man) * self.price + int(child) * self.price * 0.5
        elif day in range(6,8):
            total = int(man) * self.price * 1.2 + int(child) * self.price * 1.2 * 0.5
        else:
            print("您输入错误")
        return total
total = Ticket().caluct_cost()
print("您需要付款{0}元".format(total))

# 人和机器猜拳游戏写成一个类， 有如下几个函数
# 1)函数1:选择角色:1曹操,2张飞,3刘备
# 2)函数2:角色猜拳1剪刀2石头3布玩家输入-个1-3的数
# 3)函数3:电脑出拳随机产生1个1-3的数字，提示电脑出拳结果
# 4)函数4:角色和机器出拳对战，对战结束后，最后出示本局对战结果：赢、输，然后提示用户是否继续?按y继续，按n退出。
# 5)最后结束的时候输出结果角色赢几局电脑赢几局,平局几次游戏结束

import random

class guess_game():
    role_dict = {1:"曹操",2:"张飞",3:"刘备"}
    fist_dict = {1:"剪刀",2:"石头",3:"布"}

    def  get_Role_name(self):
        role_name = input('请输入您的角色名：1:"曹操",2:"张飞",3:"刘备"')
        return self.role_dict[int(role_name)]

    def get_role_fist(self):
        fist_num = input('请出拳：1:"剪刀",2:"石头",3:"布"')
        return int(fist_num)

    def get_computer_fist(self):
        fist_num = random.randint(1,3)
        print("电脑出拳{0}".format(fist_num))
        return int(fist_num)

    def play_game(self):
        role_win = 0
        cp_win = 0
        draw = 0
        role_name = self.get_Role_name()  #获取角色名
        while True:
            role_fist = self.get_role_fist()  #角色出拳
            computer_fist = self.get_computer_fist()    #电脑出拳
            print(role_name + "出拳为{0},电脑出拳为{1}".format(self.fist_dict[role_fist],self.fist_dict[computer_fist]))
            if role_fist - computer_fist == 1 or role_fist-computer_fist ==-2:
                role_win += 1
                print("角色赢了")
            elif role_fist - computer_fist == -1 or role_fist - computer_fist == 2:
                cp_win +=1
                print("电脑赢了")
            elif role_fist - computer_fist == 0:
                draw += 1
                print("平局")

            choose = input("您是否要继续？按y继续，按n退出")
            if choose == "n":
                break
        print("角色赢了{0}局，电脑赢了{1}局，平局{2}场".format(role_win,cp_win,draw))
if __name__ == "__main__":
    guess_game().play_game()




















#类与对象
# 软件测试工程师类
#类一般包含 属性和方法
class Teacher:
    name = "华华"
    age = "23"
    def coding(self):   #self表示实例方法
        print(self.name + "会敲代码")
    def cooking(self):
        print("会做饭")
    @classmethod
    def swimming(cls):
        print("老师还有会游泳")
    @staticmethod
    def sing():
        print("要会唱歌表演给学生看")

for i in range(100):
    Teacher()
    Teacher()
    Teacher()
#类里面方法分三种：
#实例方法：意味着这个方法只能实例来调用
t = Teacher()  #实例 隐式的传递
t.cooking()
Teacher().cooking()
Teacher.cooking(t)   #显示的传递
#类方法   @classmethod
Teacher.swimming()
t.swimming()
#静态方法   @staticmethod
Teacher.sing()
t.sing()

#1：实例方法self 类方法cls 静态方法   实例和类名都可以直接调用
#2：不同点：静态方法和类方法不可以调用类里面的属性值，如果你要参数，请自己传递参数
#3：什么时候定义为静态方法和类方法，当你的某个函数与其他的类函数 类属性没有关系
#就可以定义静态方法和类方法


class QualityAssurance:
    #属性值
    title  ="QA"
    age = "24~30"
    salary = "2W"
    expercience = "2年以上"

    def test_function(self):
        return("我会功能测试！")
    def test_auto(self):
        return("我会自动化测试")
    def test_property(self):
        return("我会性能测试！")
qa = QualityAssurance()
print("测试工程师的年龄范围是",qa.age)
print(qa.test_function())


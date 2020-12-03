#接口测试本质  就是测试类里面的函数  通过数据驱动
#单元测试的本质  测试函数  代码级别   通过代码级别

# 单元测试的框架   unitest+接口  pytest+web  --》接口
# pytest +jenkins + allure

#功能测试
# 1：写用例 TestCase
# 2：执行用例  1：TestSuite  存储用例  2：TestLoader  找用例，加载用例，存到1的TestCase
# 3：对比实际结果 期望结果  判定用例是否通过  # 断言 Assert
# 4：出具测试报告  TextTestRunner

import unittest

# 写一个测试类 对我们自己写的math method 模块里面的类  进行测试
from class_10_unitest.math_method import MathMethod


class TestMathMethod(unittest.TestCase):  #继承了unittest 里面的TestCase  专门来写用例
    #编写测试用例
    #一个用例就是一个函数 不能传参 只有self关键字
    #所有的用例 （所有的函数  都是test开头 test_）
    def test_add_two_positive(self):  #两个正数相加
        res = MathMethod(1, 1).add()  #实际发起请求的结果值
        print("1+1的结果是：",res)
        #加一个断言，判断期望值与实际值的比对结果 一致就算通过 不一致就算失败
        try:
            self.assertEqual(2,res)
        except AssertionError as e:
            print("出错啦！断言错误是{0}".format(e))
            raise e   #异常处理完之后 记得要抛出异常

    def test_add_two_zero(self):    # 两个0相加
        res = MathMethod(0, 0).add()
        print("0+0的结果是：", res)
        try:
            self.assertEqual(0, res)
        # self.assertEqual(1, res,"两个0相加出错了！")  #断言里面 msg是用例执行失败的时候才会显示
        except AssertionError as e:
            print("出错啦！断言错误是{0}".format(e))
            raise e
    def test_add_two_negative(self):  #两个负数相加
        res = MathMethod(-2, -3).add()
        print("-2+ -3的结果是：", res)
        try:
            self.assertEqual(-5, res)
        except AssertionError as e:
            print("出错啦！断言错误是{0}".format(e))
            raise e
class TestMultiMethod(unittest.TestCase):
    def test_multi_two_positive(self):  #两个正数相乘
        res = MathMethod(1, 1).multi()
        print("1+1的结果是：",res)

    def test_multi_two_zero(self):    # 两个0相乘
        res = MathMethod(0, 0).multi()
        print("0+0的结果是：", res)

    def test_multi_two_negative(self):  #两个负数相乘
        res = MathMethod(-2, -3).multi()
        print("-2+ -3的结果是：", res)

if __name__ == '__main__':
    unittest.main()

#ASCII  按照函数名，谁在前，先执行谁

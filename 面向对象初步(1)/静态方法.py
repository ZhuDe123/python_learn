'''
Python中允许定义与“类对象”无关的方法，称为“静态方法”。

“静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了“类的名字空间里面”，
需要通过“类调用”。

静态方法通过装饰器@staticmethod来定义，格式如下：
    @staticmethod
    def  静态方法名([形参列表]) ：
        函数体
要点如下：
    1.@staticmethod必须位于方法上面一行
    2.调用静态方法格式：“类名.静态方法名(参数列表)”。
    3.静态方法中访问实例属性和实例方法会导致错误
'''


class Student:
    company = "SXT"  # 类属性

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0}+{1}={2}".format(a, b, (a + b)))
        return a + b


Student.add(20, 30)

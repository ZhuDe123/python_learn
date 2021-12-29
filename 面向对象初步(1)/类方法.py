'''
类方法是从属于“类对象”的方法。类方法通过装饰器@classmethod来定义，格式如下：
    @classmethod
    def  类方法名(cls  [，形参列表]) ：
        函数体
要点如下：
    1.@classmethod必须位于方法上面一行
    2.第一个cls必须有；cls指的就是“类对象”本身；
    3.调用类方法格式：“类名.类方法名(参数列表)”。 参数列表中，不需要也不能给cls传值。
    4.类方法中访问实例属性和实例方法会导致错误
    5.子类继承父类方法时，传入cls是子类对象，而非父类对象
'''


class Student:
    company = "SXT"  # 类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)


Student.printCompany()

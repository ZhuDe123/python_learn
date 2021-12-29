'''
@property主要用于帮助我们处理属性的读操作、写操作。对于某一个属性，我们可以直接通过：
emp1.salary = 30000
如上的操作读操作、写操作。但是，这种做法不安全。
比如，我需要限制薪水必须为1-10000的数字。这时候，我们就需要通过getter、setter方法来处理。
'''


# 测试@property
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property  # 相当于salary属性的getter方法
    def salary(self):
        print("月薪为{0},年薪为{1}".format(self.__salary, (12 * self.__salary)))
        return self.__salary

    @salary.setter
    def salary(self, salary):  # 相当于salary属性的setter方法
        if (0 < salary < 1000000):
            self.__salary = salary
        else:
            print("薪水录入错误！只能在0-1000000之间")


emp1 = Employee("高淇", 100)
print(emp1.salary)

emp1.salary = -200

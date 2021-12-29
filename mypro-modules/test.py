import Salary
from a.aa.module_AA import fun_AA
# math.sin()
print(Salary.__doc__)
print(Salary.daySalary.__doc__)
print(Salary.__name__)

# import calculator
#
# c = calculator.add(4, 5)
# print(c)
# add(100,200) #不加模块名无法识别
from calculator import add

c = add(1, 2)  # 无需模块名，可以直接引用里面的函数/类
print(c)


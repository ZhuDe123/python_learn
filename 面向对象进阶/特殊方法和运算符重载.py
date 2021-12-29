'''
Python的运算符实际上是通过调用对象的特殊方法实现的。比如：
方法	说明	例子
__init__	        构造方法	    对象创建：p = Person()
__del__	            析构方法	    对象回收
__repr__,__str__ 	打印，转换  	print(a)
__call__	        函数调用	    a()
__getattr__	        点号运算	    a.xxx
__setattr__	        属性赋值	    a.xxx = value
__getitem__	        索引运算	    a[key]
__setitem__ 	    索引赋值 	a[key]=value
__len__	            长度	        len(a)
'''

a = 20
b = 30
c = a + b
d = a.__add__(b)
print("c=", c)
print("d=", d)

'''我们可以重写上面的特殊方法，即实现了“运算符的重载”。'''


# 测试运算符的重载


class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}--{1}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other, int):
            return self.name * other
        else:
            return "不是同类对象，不能相乘"


p1 = Person("高淇")
p2 = Person("高希希")

x = p1 + p2
print(x)

print(p1 * 3)

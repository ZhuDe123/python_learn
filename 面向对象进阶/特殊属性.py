'''
Python对象中包含了很多双下划线开始和结束的属性，这些是特殊属性，有特殊用法。
这里我们列出常见的特殊属性：

特殊方法	含义
obj.__dict__	对象的属性字典
obj.__class__	对象所属的类
class.__bases__	类的基类元组（多继承）
class.__base__	类的基类
class.__mro__	类层次结构
class.__subclasses__()	子类列表

'''


# 测试特殊属性
class A:
    pass


class B:
    pass


class C(B, A):

    def __init__(self, nn):
        self.nn = nn

    def cc(self):
        print("cc")


c = C(3)

print("dir(c):\t", dir(c))
print("c.__dict__:\t", c.__dict__)
print("c.__class__:\t", c.__class__)
print("C.__bases__:\t", C.__bases__)
print("C.mro():\t", C.mro())
print("A.__subclasses:\t", A.__subclasses__())

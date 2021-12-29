'''
object有一个__str__()方法，用于返回一个对于“对象的描述”，
对应于内置函数str()经常用于print()方法，帮助我们查看对象的信息。__str__()可以重写。
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        '''将对象转化成一个字符串，一般用于print方法'''
        return "名字是：{0},年龄是{1}".format(self.name, self.__age)


p = Person("高淇", 18)
print(p)

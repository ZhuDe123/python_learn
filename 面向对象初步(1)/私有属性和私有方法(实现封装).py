'''
Python对于类的成员没有严格的访问控制限制，这与其他面向对象语言有区别。关于私有属性和私有方法，有如下要点：
    1.通常我们约定，两个下划线开头的属性是私有的(private)。其他为公共的(public)。
    2.类内部可以访问私有属性(方法)
    3.类外部不能直接访问私有属性(方法)
    4.类外部可以通过“_类名__私有属性(方法)名”访问私有属性(方法)

【注】方法本质上也是属性！只不过是可以通过()执行而已。
所以，此处讲的私有属性和公有属性，也同时讲解了私有方法和公有方法的用法。
如下测试中，同时也包含了私有方法和公有方法的例子。
'''


# 测试私有属性、私有方法
class Employee:
    __company = "百战程序员"  # 私有类属性.   通过dir可以查到_Employee__company

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有实例属性

    def say_company(self):
        print("我的公司是：", Employee.__company)  # 类内部可以直接访问私有属性
        print(self.name, "的年龄是：", self.__age)
        self.__work()

    def __work(self):  # 私有实例方法   通过dir可以查到_Employee__work
        print("工作！好好工作，好好赚钱，娶个媳妇！")


p1 = Employee("高淇", 32)
print(p1.name)
print(dir(p1))  #
p1.say_company()
print(p1._Employee__age)  # 通过这种方式可以直接访问到私有属性  。通过dir可以查到属性：_Employee__age
# print(p1.__age)           #直接访问私有属性，报错
# p1.__work()             #直接访问私有方法，报错

'''
从打印的Person对象所有属性我们可以看出。
私有属性“__age”在实际存储时是按照“_Person__age”这个属性来存储的。
这也就是为什么我们不能直接使用“__age”而可以使用“_Person__age”的根本原因。
'''
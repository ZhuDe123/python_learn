'''
“is-a”关系，我们可以使用“继承”。从而实现子类拥有的父类的方法和属性。
    “is-a”关系指的是类似这样的关系：狗是动物，dog is animal。狗类就应该继承动物类。
“has-a”关系，我们可以使用“组合”，也能实现一个类拥有另一个类的方法和属性。
    ”has-a”关系指的是这样的关系：手机拥有CPU。 MobilePhone has a CPU。
'''


# 组合测试

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:

    def calculate(self):
        print("计算，算个12345")


class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的钛合金大眼")


c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()  # 通过组合，我们也能调用cpu对象的方法。相当于手机对象间接拥有了“cpu的方法”
m.screen.show()

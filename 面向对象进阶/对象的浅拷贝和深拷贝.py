'''
·变量的赋值操作
    只是形成两个变量，实际还是指向同一个对象。
·浅拷贝
    Python拷贝一般都是浅拷贝。拷贝时，对象包含的子对象内容不拷贝。
    因此，源对象和拷贝对象会引用同一个子对象。
·深拷贝
    使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象。
    源对象和拷贝对象所有的子对象也不同。
'''

# 测试对象的引用赋值、浅拷贝、深拷贝
import copy


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:

    def calculate(self):
        print("计算，算个12345")
        # print("CPU对象:", self)


class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的钛合金大眼")
        # print("屏幕对象：", self)


c = CPU()
s = Screen()
m = MobilePhone(c, s)

m.cpu.calculate()

n = m  # 两个变量，但是指向了同一个对象
print(m, n)
print("id(m)==id(n)", id(m) == id(n))
print("id(m.cpu) == id(n.cpu)", id(m.cpu) == id(n.cpu))
print("id(m.screen) == id(n.screen)", id(m.screen) == id(n.screen))

m2 = copy.copy(m)  # m2是新拷贝的另一个手机对象
print(m, m2)
print("id(m)==id(m2)", id(m) == id(m2))
print("id(m.cpu) == id(m2.cpu)", id(m.cpu) == id(m2.cpu))
print("id(m.screen) == id(m2.screen)", id(m.screen) == id(m2.screen))

m.cpu.calculate()
m2.cpu.calculate()  # m2和m拥有了一样的cpu对象和screen对象

m3 = copy.deepcopy(m)
m3.cpu.calculate()  # m3和m拥有不一样的cpu对象和screen对象
print("id(m)==id(m3)", id(m) == id(m3))
print("id(m.cpu) == id(m3.cpu)", id(m.cpu) == id(m3.cpu))
print("id(m.screen) == id(m3.screen)", id(m.screen) == id(m3.screen))

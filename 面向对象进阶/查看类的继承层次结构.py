'''
通过类的方法mro()或者类的属性__mro__可以输出这个类的继承层次结构。
'''


class A: pass


class B(A): pass


class C(B): pass


print(C.mro())

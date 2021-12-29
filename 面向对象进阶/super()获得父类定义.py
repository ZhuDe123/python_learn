'''
在子类中，如果想要获得父类的方法时，我们可以通过super()来做。
super()代表父类的定义，不是父类对象。
'''


class A:
    def say(self):
        print("A: ", self)
        print("say AAA")


class B(A):
    def say(self):
        # A.say(self)    调用父类的say方法
        super().say()  # 通过super()调用父类的方法
        print("say BBB")


b = B()
b.say()

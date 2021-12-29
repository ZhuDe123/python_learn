'''
Python中，“一切都是对象”。实际上，执行def定义函数后，系统就创建了相应的函数对象。
我们执行如下程序，然后进行解释：
'''


def print_star(n):
    print("*" * n)


print(print_star)
print(id(print_star))

c = print_star

print("c的id={0}".format(id(c)))
c(3)

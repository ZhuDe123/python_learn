'''
return返回值要点：
1.如果函数体中包含return语句，则结束函数执行并返回值；
2.如果函数体中不包含return语句，则返回None值。
3.要返回多个返回值，使用列表、元组、字典、集合将多个值“存起来”即可。
'''


# 定义一个打印n个星号的无返回值的函数
def print_star(n):
    print("*" * n)


print_star(5)


# 定义一个返回两个数平均值的函数
def my_avg(a, b):
    return (a + b) / 2


# 如下是函数的调用
c = my_avg(20, 30)
print(c)

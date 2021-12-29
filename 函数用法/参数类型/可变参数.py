'''
可变参数指的是“可变数量的参数”。分两种情况：
1.*param（一个星号），将多个参数收集到一个“元组”对象中。
2.**param（两个星号），将多个参数收集到一个“字典”对象中。
'''


# 测试可变参数处理（元组、字典两种方式）
def f1(a, b, *c):
    print(a, b, c)


f1(8, 9, 19, 20)


def f2(a, b, **c):
    print(a, b, c)


f2(8, 9, name='gaoqi', age=18, job="teacher")


def f3(a, b, *c, **d):
    print(a, b, c, d)


f3(8, 9, 20, 30, 40, name='gaoqi', age=18)

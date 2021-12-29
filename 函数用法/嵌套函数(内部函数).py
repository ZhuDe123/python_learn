'''
嵌套函数：
在函数内部定义的函数！
'''


def f1():
    print('f1 running...')

    def f2():
        print('f2 running...')

    f2()


f1()

'''
上面程序中，f2()就是定义在f1函数内部的函数。f2()的定义和调用都在f1()函数内部。


一般在什么情况下使用嵌套函数？
1.封装 - 数据隐藏
外部无法访问“嵌套函数”。
2.贯彻 DRY(Don’t  Repeat  Yourself) 原则
嵌套函数，可以让我们在函数内部避免重复代码。
3.闭包
后面会详细讲解。
'''


# 使用嵌套函数避免重复代码
def printChineseName(name, familyName):
    print("{0} {1}".format(familyName, name))


def printEnglishName(name, familyName):
    print("{0} {1}".format(name, familyName))


# 使用1个函数代替上面的两个函数
def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print("{0} {1}".format(a, b))

    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)


printName(True, "小七", "高")
printName(False, "George", "Bush")

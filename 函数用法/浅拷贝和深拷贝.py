'''
为了更深入的了解参数传递的底层原理，我们需要讲解一下“浅拷贝和深拷贝”。
我们可以使用内置函数：copy(浅拷贝)、deepcopy(深拷贝)。

浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用。
深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象
'''

# 测试浅拷贝和深拷贝

import copy


def testCopy():
    '''测试浅拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝......")
    print("a", a)
    print("b", b)


def testDeepCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("深拷贝......")
    print("a", a)
    print("b", b)


testCopy()
print("*************")
testDeepCopy()
print("*************")

# 传递不可变对象时。不可变对象里面包含的子对象是可变的。
# 则方法内修改了这个可变对象，源对象也发生了变化。

a = (10, 20, [5, 6])
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


test01(a)
print("test01(a):",a)

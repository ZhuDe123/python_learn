'''
我们在前面讲的类定义格式中，“class  类名：”。
实际上，当解释器执行class语句时，就会创建一个类对象。
'''

class Student:
    pass  # 空语句


print(type(Student))
print(id(Student))

Stu2 = Student
s1 = Stu2()
print(s1)

'''
我们可以看到实际上生成了一个变量名就是类名“Student”的对象。
我们通过赋值给新变量Stu2，也能实现相关的调用。说明，确实创建了“类对象”。

【注】pass为空语句。就是表示什么都不做，只是作为一个占位符存在。
当你写代码时，遇到暂时不知道往方法或者类中加入什么时，可以先用pass占位，后期再补上。
'''

'''
Python是动态语言，我们可以动态的为类添加新的方法，或者动态的修改类的已有的方法。
'''


# 测试方法的动态性
class Person:
    def work(self):
        print("努力上班！")


def play_game(self):
    print("{0}玩游戏".format(self))


def work2(s):
    print("好好工作，努力上班！")


Person.play = play_game
Person.work = work2
p = Person()
p.play()
p.work()
'''我们可以看到，Person动态的新增了play_game方法，以及用work2替换了work方法。'''
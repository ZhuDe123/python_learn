score = int(input("请输入分数"))
grade = ''
if (score < 60):
    grade = "不及格"
if (60 <= score < 80):
    grade = "及格"
if (80 <= score < 90):
    grade = "良好"
if (90 <= score <= 100):
    grade = "优秀"

print("分数是{0},等级是{1}".format(score, grade))

score = int(input("请输入分数"))
grade = ''
if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
elif score <= 100:
    grade = "优秀"

print("分数是{0},等级是{1}".format(score, grade))

x = int(input("请输入x坐标"))
y = int(input("请输入y坐标"))

if (x == 0 and y == 0):
    print("原点")
elif (x == 0):
    print("y轴")
elif (y == 0):
    print("x轴")
elif (x > 0 and y > 0):
    print("第一象限")
elif (x < 0 and y > 0):
    print("第二象限")
elif (x < 0 and y < 0):
    print("第三象限")
else:
    print("第四象限")

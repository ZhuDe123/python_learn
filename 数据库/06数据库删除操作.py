import pymysql

db = pymysql.connect(host="localhost", user="root", password="zds13938431145", database="pythontest")

cursor = db.cursor()

sql = "delete from student where age < 22"

try:
    cursor.execute(sql)
    db.commit()
    print("delete success")
except Exception as e:
    print(e)
    print("修改失败")
    db.rollback()
finally:
    db.close()

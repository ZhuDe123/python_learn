import pymysql

db = pymysql.connect(host="localhost", user="root", password="zds13938431145", database="pythontest")

cursor = db.cursor()

sql = "update student set score=%s where sno=%s; "

try:
    cursor.execute(sql, (98, 3))
    db.commit()
    print("success")
except Exception as e:
    print(e)
    print("修改失败")
    db.rollback()
finally:
    db.close()

import mysql.connector as mysql

db = mysql.connect(
           host = "localhost",
           user = "root",
           passwd = "",
           database = "student"

        )
cursor=db.cursor()

try:
    cursor.execute("INSERT INTO students VALUES('','sudhir',23)" )
    db.commit()
    print("data inserted")
    cursor.execute("SELECT*FROM students")
    data=cursor.fetchall()
    for i in data:
     print(i)
    
      
except:
    print("data insertion problem")


print(db)
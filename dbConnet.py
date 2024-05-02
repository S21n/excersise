import mysql.connector as mysql

db = mysql.connect(
           host = "localhost",
           user = "root",
           passwd = "",
           database = "student"

        )
cursor=db.cursor()

try:
    cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
    print("tables created")
      
except:
    print("tables not created")


print(db)
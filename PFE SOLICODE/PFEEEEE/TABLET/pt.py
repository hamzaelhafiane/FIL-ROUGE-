import pymysql
while True:
  mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="demo"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT st, usernamecl FROM myguests")
  myresult = mycursor.fetchall()
  print(myresult)
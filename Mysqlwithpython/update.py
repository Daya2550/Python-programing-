import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
    user="root",
    password="2550",
    database="data"
)

d=mydb.cursor()
d.execute("update info set id = 1 where id=2")
d.execute("select *  from info")
r=d.fetchall()
for i in r:
     print(i)

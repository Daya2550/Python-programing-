import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2550",
    database="data"
)

d=mydb.cursor()
d.execute("select * from info")
r=d.fetchall()
for i in r:
    print(i)
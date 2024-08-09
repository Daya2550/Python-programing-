import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2550",
    database="data"
)

d=mydb.cursor()
d.execute("CREATE DATABASE if not exists data")
d.execute("create table if not exists info (id int primary key,name varchar(50),age int )")
d.execute("SHOW TABLES")
for i in d:
    print(i)
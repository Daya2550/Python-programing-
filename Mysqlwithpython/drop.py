import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2550",
    database="data"
)
d=mydb.cursor()
d.execute("drop table info")
d.execute("drop database data")
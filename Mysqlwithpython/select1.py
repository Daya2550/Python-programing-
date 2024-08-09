import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2550",
    database="data"
)

d = mydb.cursor()
d.execute("SELECT * FROM info")
r = d.fetchall()

for x in r:
    print(x)

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2550",
    database="data"
)

d=mydb.cursor()


q="insert into info (id,name,age) values (%s,%s,%s)"
data=(2,"Rahul desur",20)






d.execute(q,data)
mydb.commit()


val = [
  (3,'Peter', 21),
  (4,'Amy', 22),
  
]

d.executemany(q,val)
mydb.commit()
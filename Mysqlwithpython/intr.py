import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2550"
  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE data")

       

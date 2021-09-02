import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gowtham@9885",
  database="world"
)

mycursor=mydb.cursor()

#mycursor.execute("show databases")

mycursor.execute("select * from city")
for i in mycursor:
  print(i)
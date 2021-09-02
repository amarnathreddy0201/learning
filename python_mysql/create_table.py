import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gowtham@9885",
  database="world"
)

mycursor = mydb.cursor()

""" 
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
this two for creating table
mycursor.execute("CREATE TABLE people (name varchar(50) not null, age int not null, address varchar(250))")
"""

"""
printing the tables
mycursor.execute("show tables")#for showing tables
for x in mycursor:
  print(x)
"""


mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE custom (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("ALTER TABLE customers ADD COLUMN sno INT")



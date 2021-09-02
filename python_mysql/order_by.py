import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowtham@9885",
    database="world"
)


cursor=mydb.cursor()
"""
cursor.execute("show tables")
for i in cursor:
    print(i)
"""
sql="select * from country"
cursor.execute(sql)
result=cursor.fetchall()
for i in result:
    print(i)


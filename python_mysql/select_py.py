"""
one more time we will check
"""


import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowtham@9885",
    database="world"
)

mycursor=mydb.cursor(buffered=True)

mycursor.execute("show tables")
for i in mycursor:
    print(i)
    mycursor.execute("select * from {}".format(i))
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    print()
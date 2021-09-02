import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gowtham@9885",
  database="world"
)

mycursor = mydb.cursor()
sql="insert into customers (name, address) values(%s, %s)"
val=[("amar", "rayalasheema"),
     ("nath", "kurnool"),
     ("reddy", "kolimigundla"),
     ('Hannah', 'Mountain 21'),
     ('Michael', 'Valley 345'),
     ('Sandy', 'Ocean blvd 2'),
     ('Betty', 'Green Grass 1'),
     ('Richard', 'Sky st 331'),
     ('Susan', 'One way 98'),
     ('Vicky', 'Yellow Garden 2'),
     ('Ben', 'Park Lane 38'),
     ('William', 'Central st 954'),
     ('Chuck', 'Main Road 989'),
     ('Viola', 'Sideway 1633')
     ]
mycursor.executemany(sql,val)

mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("select * from customers")
for i in mycursor:
    print(i)
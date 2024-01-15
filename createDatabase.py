import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="hana")

mycursor = db.cursor()
mycursor.execute("show databases")
for b in mycursor:
   print(b)

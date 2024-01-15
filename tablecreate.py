import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="hana",database="nnnnnnn")

mycursor = db.cursor()
mycursor.execute("show tables")
for b in mycursor:
   print(b)


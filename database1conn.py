import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="hana")

mycursor = con.cursor()
mycursor.excute()
for db in mycursor:
    print(db)

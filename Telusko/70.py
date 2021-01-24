import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "Tuhin", passwd = "tuuhin5084")

mycursor = mydb.cursor()

mycursor.execute("show databases")


for i in mycursor:

    print(i)
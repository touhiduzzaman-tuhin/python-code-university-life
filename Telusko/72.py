import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "tuuhin5084"
                               , database = "student")

mycursor = mydb.cursor()

mycursor.execute("select * from users")

result = mycursor.fetchall()

for i in result:

    print(i)
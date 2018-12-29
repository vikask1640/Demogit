import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="vikas",passwd="1234",database="business")

mycursor=mydb.cursor()

sql = "INSERT INTO student (name, college_name) VALUES (%s, %s)"
val = ("John", "kkichv")
mycursor.execute(sql,val)
#result=mycursor.fetchall()
#for i in mycursor:
   # print(i)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

#insert into a table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
sql="INSERT INTO employees (name,address) VALUES(%s,%s)"
val=('jagadeesh','bangalore')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'record got inserted into a table')


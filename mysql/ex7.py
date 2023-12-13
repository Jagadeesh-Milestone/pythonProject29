#insert many records:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
sql="INSERT INTO users (name,address) VALUES(%s,%s)"
val=[('jagadeesh','bangalore'),('hari','hyderabad'),
     ('suresh','chennai'),('manoj','hyderabad'),('vamsi','chennai')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'records got inserted into table')
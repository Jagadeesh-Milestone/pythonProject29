#update records
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
#mycursor.execute('UPDATE users SET address="mumbai" WHERE address="chennai"')
mycursor.execute('UPDATE users SET name="harinath" WHERE name="hari"')
mydb.commit()
print(mycursor.rowcount,'rows got updated')
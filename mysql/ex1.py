#python-mysql
#to connect mysql to python open cmd and type
#pip install mysql-connector-python.
#pip stands for python install package.
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
print('connected to mysql successfully')
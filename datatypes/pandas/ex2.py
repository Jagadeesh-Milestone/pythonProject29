#pandas series:
import pandas
x=[10,20,30,40]
y=pandas.Series(x)
print(y)
print(y[0])
#print(y[10])

#labels:
z=[100,200,300,400]
a=pandas.Series(z,index=['a','b','c','d'])
print(a)
print(a['a'])
#print(a['z'])
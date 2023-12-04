import datetime
x=datetime.date(2020,12,31)
print(x)
print(x.year)
print(x.month)
print(x.day)
y=datetime.time(11,20,36)
print(y)
print(y.hour)
print(y.minute)
print(y.second)

z=datetime.datetime.combine(x,y)
print(z)
#date and time:
import  datetime
import time

#to display current date and time
a=datetime.datetime.now()
print(a)

b=time.localtime()
print(b)

#short form of week day
c=time.strftime('%a',b)
print(c)

#full form of week day
d=time.strftime('%A',b)
print(d)

#short form of month
e=time.strftime('%b',b)
print(e)

#full form of month
f=time.strftime("%B",b)
print(f)

#week of the year.
g=time.strftime('%W',b)
print(g)

#day number of the week monday as 1.
h=time.strftime('%w',b)
print(h)

#hours in 24 hours format.possible values are 00-23
i=time.strftime('%H',b)
print(i)

#the day of the year possible values are 1-366
j=time.strftime('%j',b)
print(j)

#month number.possible values are 1-12
k=time.strftime('%m',b)
print(k)

#minutes the possible values are 0-59
l=time.strftime('%M',b)
print(l)

#seconds the possible values are 0-59
m=time.strftime('%S',b)
print(m)

#century
n=time.strftime('%C',b)
print(n)

#local version of time
o=time.strftime('%x',b)
print(o)

#local time version
p=time.strftime('%X',b)
print(p)

#am/pm
q=time.strftime('%p',b)
print(q)

#time zone
r=time.strftime('%z',b)
print(r)

#day of the month:
s=time.strftime('%d',b)
print(s)

#short form of the year
t=time.strftime('%y',b)
print(t)

#full form of the year
u=time.strftime('%Y',b)
print(u)

#hours possible values are 1-12
v=time.strftime('%I',b)
print(v)

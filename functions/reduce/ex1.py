#reduce:
from functools import reduce
x=[10,20,30,40,50,60]

def d1(a,b):
    return a+b
x=reduce(d1,x)
print(x)

x=10
y='hello'
print(x*y)
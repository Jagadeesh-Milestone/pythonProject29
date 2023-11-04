#tuple:
#a tuple is a collection/sequence of data and this data may be any type.
#a tuple allows duplicate values index calling and index slicing.
#a tuple is immutable meaning that we cant change the data.
#a tuple is having ordered elements.
#tuple is taken in ().
t=()
print(t)
print(type(t))

a=(10,20,30,10.2,True)
print(a)

#len:
b=(10,20,30)
print(len(b))

#count:
c=(10,2,3,4,10,10)
print(c.count(10))

#duplicate values.
d=(10,20,30,10,10)
print(d)

#concatenation:
#adding a tuple to another tuple.
e=(10,20,30)
f=(40,50,10)
print(e+f)
print(e+(100,200,300))

x=(10)
print(x)
print(type(x))

y=(10,)
print(y)
print(type(y))
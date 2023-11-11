#frozen set:
#it is the immutable version of set.
#we cant create a frozenset individually we have to create it from
#already existing set.
a={10,20,30}
a.pop()
print(a)

b=frozenset(a)
print(b)
#b.pop()
#print(b)

l=[1,3,5,6]
x=frozenset(l)
print(x)
x.append(100)
print(x)
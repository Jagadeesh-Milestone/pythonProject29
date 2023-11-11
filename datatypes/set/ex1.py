#set:
#a set is a collect of data and this data may be any type.
#set is having unordered elements.
#set dont allow duplicate values,index calling,index slicing.
#set is mutable.
#set is taken in {}.
s={10}
print(s)
print(type(s))

a={10,10.2,True,20,'bangalore'}
print(a)

#dupliactes are not allowed.
b={10,20,10,30,20}
print(b)

#len:
c={1,2,3,4,2,3,7,8}
print(len(c))

#no index calling:
#d={10,20,30}
#print(d[0])

#add:
e={1,5,8,6,3}
e.add(100)
print(e)

#update:
f={10,30,70,60}
f.update({50,60})
print(f)

#remove:
g={3,8,6,9}
g.remove(6)
print(g)

#discard:
h={100,200,300}
h.discard(200)
print(h)

#difference between remove and discard:
i={10,20,30,40}
#i.remove(100)#key error
i.discard(200)#no error
print(i)

#pop:
#any element will be removed from a set
j={2,3,8,9}
j.pop()
print(j)

#clear:
k={10,20,30}
k.clear()
print(k)

#copy:
l={3,4,5,6}
m=l.copy()
print(m)

#uion:
n={10,20,30,40}
o={30,50,40,60}
print(n.union(o))

#intersection:
p={10,20,30,40}
q={20,30,50,60}
print(p.intersection(q))

#difference:
r={10,20,30,40,100}
s={40,50,10,20}
print(r.difference(s))

#is subset:
a={1,2,3,5,6}
b={1,2,3,4,5,6,7,8}
print(a.issubset((b)))

#is superset
c={10,30,40,20}
d={10,20}
print(c.issuperset(d))

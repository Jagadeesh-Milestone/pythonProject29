#sequences:
#list:
#a list is a collection/sequence of data and this data may be any type.
#a list allows duplicate values,index calling and index slicing.
#a list is mutable meaning that we can change the data.
#a list is having ordered elements.
#list is taken in [].
#empty list:
a=[]
print(a)
print(type(a))

#list allows different datatypes.
b=[10,10.8,'hello',True,5+6j,[10,20]]
print(b)
print(type(b))

#list allows duplicate values.
c=[10,20,30,10,10]
print(c)

#repetetion
d=[10,20,30,40]
print(d*3)

#index position:
#the index position of first element of a list is always '0', second
#element is '1',....
e=[100,200,300,400]
print(e.index(400))
#print(e.index(500))

#we can call the value at a particular index position:
print(e[0])
print(e[3])
#print(e[4])

#negative index:
#the negative index will be from right ti left side
#index position of first element is -1,second element is -2...
f=[10,20,30,40]
print(f[-1])
#print(f[-5])

#append:
#it is used to add an element at the end of a list.
g=[100,200,300,400]
g.append(500)
print(g)

#pop:
#it is used to remove an element from the end of a list:
h=[1,2,3,4]
h.pop()
print(h)

#we can remove particular element by using index position.
h.pop(0)
print(h)

#extend:
#it is used to add multiple values at the end of a list.
i=[10,20,60,80]
i.extend([100,200])
print(i)

#len:
#it is used to find the no of values in a list.
j=[10,20,30,40,50]
print(len(j))

#count:
#it is used to find the no of appearances of a value
k=[1,2,3,4,2,3,2]
print(k.count(2))
print(k.count(100))

#insert:
#it is used to add an element at a particular index position.
l=[100,200,400,500]
l.insert(2,300)
print(l)
l.insert(0,[1000,3000])
print(l)

#copy:
#it is used to store the copy a list.
m=[1,2,3,4]
n=m.copy()
print(n)

#clear:
#it is used to clear the list elements.
o=[100,200,300]
o.clear()
print(o)

#remove:
#it is used to remove an element directly from the list.
p=[10,20,30,100]
p.remove(20)
print(p)
#p.remove(200)
#print(p)

#reverse.
#it is used to reverse the list of elements.
q=[10,20,40,20,30]
q.reverse()
print(q)

#sort.
#it is used to print the list of elements in ascending and descending order.
r=[1,4,7,2,3,9,5]
r.sort(reverse=False)
print(r)
r.sort(reverse=True)
print(r)


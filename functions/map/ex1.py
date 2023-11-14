#map:
l=[10,20,30,40,50]
print(l*2)
for i in l:
    print(i*2,end=" ")

#map(function ,iterable)
def d1(m):
    return m*3
m=map(d1,l)
print(list(m))

#using map in lambda
x=map(lambda n:n*2,l)
print(list(x))
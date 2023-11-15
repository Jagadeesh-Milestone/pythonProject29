#filter:
l=[1,2,3,4,5,6,7]
for i in l:
    if i%2==1:
        print(i,end=" ")

def d1(m):
    return m%2==0
f=filter(d1,l)
print(list(f))

x=filter(lambda c:c%2==1,l)
print(tuple(x))
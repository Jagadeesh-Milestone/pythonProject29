l1=[1,2,3,4,5,6]
l2=[5,6,7,8]

def d2(m,n):
    return m*n
x=map(d2,l1,l2)
print(list(x))

y=map(lambda a,b:a*b,l1,l2)
print(tuple(y))
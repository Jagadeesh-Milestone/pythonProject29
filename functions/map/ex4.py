l=['bangalore','mumbai','chennai','hyderabad']
for i in l:
    print(i[::-1])

def d1(a):
    return a[::-1]
m=map(d1,l)
print(list(m))

x=map(lambda b:b[::-1],l)
print(tuple(x))
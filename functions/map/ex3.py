l=['bangalore','mumbai','chennai','hyderabad']
print(len(l))
for i in l:
    print(len(i))

def d1(m):
    return len(m)
m=map(d1,l)
print(list(m))

s=map(lambda n:len(n),l)
print(tuple(s))
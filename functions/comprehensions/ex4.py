#dict comprehensions:
d={}
l=[1,2,3,4,5,6,7]
for i in l:
    d[i]=i*i
print(d)

y={i:i*3 for i in l}
print(y)
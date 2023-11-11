#list comprehension:
x=[]
for i in range(1,10):
    x.append(i*i)
print(x)

y=[i*i for i in range(2,10)]
print(y)
#comprehensions:
l=[1,2,3,4,5,6,7,8,9]
x=[]
for i in l:
    if i%2==1:
        x.append(i)
print(x)

#using list comprehension:
y=[i for i in l if i%2==0]
print(y)
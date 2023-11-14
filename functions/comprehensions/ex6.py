#generator comprehension:
l=[1,2,3,4,5,6,7,8]
m=(i for i in l if i%2==0)
print('generator comprehension values:',end="")

for i in m:
   print(i,end=" ")
print(type(m))

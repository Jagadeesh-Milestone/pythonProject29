#for:
#it is used when the user knows the exact output:
#normally for loop is used on iterables:
l=[10,20,30,40]
for i in l:
    print(i)
#break:
x=(1,2,3,4,4,5,6,7)
for a in x:
    print(a)
    if a==5:
        break

#continue:
y='bangalore'
for m in y:
    if m=='g':
        continue
    print(m)
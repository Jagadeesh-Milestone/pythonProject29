#list comprehension:
x=['hello','python','milestone','bangalore']
y=[]
for i in x:
    if 'l' in i:
        y.append(i)
print(y)

z=[i for i in x if 'e' in i]
print(z)
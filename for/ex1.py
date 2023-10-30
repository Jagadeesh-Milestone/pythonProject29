#for:
#for loop is used when the user knows exact output:
#it will be used on sequences.
l=[10,20,30,40]
for i in l:
    print(i)

#break:
#it is used to break the loop when the certain condition is met.
x=[10,20,30,40,50,60]
for i in x:
    print(i)
    if i==40:
        break

#continue:
#it is used to skip the current condition and continue with the
# remaining statements
s="hyderabad"
for i in s:
    if i=='r':
        continue
    print(i,end=" ")
#end="" is used to print the looping objects in a single line

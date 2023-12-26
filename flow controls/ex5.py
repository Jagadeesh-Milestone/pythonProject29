#loops:
#loops are used when you have perform a single task multiple times.
#while
#for
#while loop:
#it is used when the user does not knows the exact output:
i=0
while i<10:
    print(i)
    i+=1
#break:
#it is used to break the loop when the loop meets a particular
#condition:
i=10
while i<20:
    print(i)
    if i==13:
        break
    i+=1

#continue:
#it is used to continue with the other statements and skip the
#current condition:
i=20
while i<30:
    i+=1
    if i==25:
        continue
    print(i)
#no of digits in a number:
number=int(input('enter any number:'))
count=0
while number!=0:
    number//=10
    count+=1
print('the no of digits in the given number are',count)

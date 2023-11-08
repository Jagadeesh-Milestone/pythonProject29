#display all the prime numbers between 1-100:
lower=1
upper=100
print('prime numbers between',lower,'and',upper,'are:')
for number in range(lower,upper+1):
    if number>1:
       for i in range(2,number):
           if number%i==0:
               break
       else:
           print(number)

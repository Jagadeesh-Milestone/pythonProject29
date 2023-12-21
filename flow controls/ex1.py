#flow controls/conditional statements.
#these are used to control the flow of a program.
#if
#else
#elif
#nested if
#if:
#if returns true when the given statement is true.
a=10
if a==10:
    print('condition is true')
    l=[10,20,30,40]
    print(l)
else:
    print('condition is false')
    t=(10,20,30,40)
    print(t)

name='jagadeesh'
if name=='jagadeesh':
    print('name is correct')
else:
    print('name is wrong')

username='chinna'
pin=890890
if username=='chinna' and pin==890890:
    print('login success')
else:
    print('login failed')

username='chinna'
pin=890890
if username=='china' or pin==890891:
    print('login successful')
else:
    print('login failure')

#usernames=['hari','jagadeesh','mahesh','uday']
#user=input('enter your name:')
#if user in usernames:
 #   print('your name in list')
#else:
  #  print('your name not in list')

#city=input('enter your city name:')
#zipcode=int(input('enter your city zipcode:'))
#if city=='dellas' and zipcode==563322:
#    print('you are in dellas')
#else:
 #   print('you are outside dellas')

#pass
#it is used to fill the empty blocks.
x=10
if x==10:
    print('if condition executed')
else:
    pass
#variables:
#in python there are three types of variables
#global variable
#local variable
#protected variable
#global variable:
#when you declare a variable globally we can access it anywhere
#in the program.
a=100
print('a value before the function:',a)
def d1():
    print('a value inside the function:',a)
d1()
print('a value after the function:',a)


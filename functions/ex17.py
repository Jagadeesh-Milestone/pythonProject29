#global keyword:
#it is used to access the local variable globally.
x=100
print('x value before the function:',x)
def d1():
    global x
    x=200
    print('x value inside the function:',x)
d1()
print('x value after the function:',x)
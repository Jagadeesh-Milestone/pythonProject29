#globals method:
#when the global variable and local variable have same name
#to access global value locally we use globals method:

x=100
print('x value before the function:',x)
def d1():
    x=200
    print('x value inside the function:',x)
    print('x value before the function:',globals()['x'])
d1()
print('x value after the function:',x)

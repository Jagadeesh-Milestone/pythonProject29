#local variable:
#if declare a variable locally(inside the function) we can use it
#within that function only we cant use it outside the function:

#print('x value before the function:',x)
def d1():
    #print(x)#x value not assigned yet
    x=100
    print('x value inside the function:',x)
    print(x)
d1()
#print('x value after the function:',x)
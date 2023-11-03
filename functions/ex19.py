
#we cant use the arguments of inner function in outer function:
def d1():
    print(a*b)
    def d2(a,b):
        print(a+b)
    d2(5,6)
d1()

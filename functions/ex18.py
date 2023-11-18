
#we can use the arguments of outer function inside inner function.
def d1(a,b):
    c=100
    print(c)
    #print(x)
    def d2():
        return a+b
    x=200
    print(x)
    print(c)
    return d2()

d=d1(20,30)
print(d)

#we can use the arguments of outer function inside inner function.
def d1(a,b):
    def d2():
        return a+b
    return d2()
d=d1(20,30)
print(d)
#closure:
#a closure is a python function which satisfies the following
#three conditions.
#a function must be taken inside another function.
#a function must be returned.
#a function is sended to a variable.
def d1(a,b):
    print(a+b)
    def d2(c,d):
        return c*d
    return d2(10,4)
d=d1(30,40)
print(d)
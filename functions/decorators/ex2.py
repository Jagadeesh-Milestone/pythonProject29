#it is used to add extra functionality to existing function.
def d1(func):
    def d2(a):
        result=func(a*a)
        return result
    return d2
@d1
def d3(a):
    return a
d=d3(20)
print(d)

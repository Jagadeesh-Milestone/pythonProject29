#returning a function:
#we can return a function like we return the expression.
def d1():
    def d2():
        return 'hello world'
    return d2()
d=d1()
print(d)

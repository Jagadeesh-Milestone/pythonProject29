#nested function with arguments
def d1(a,b):
    print(a+b)
    def d2(c,d):
        print(c*d)
    d2(4,5)
d1(10,20)


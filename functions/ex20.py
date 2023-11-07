#global scope.
def d1():
    print('hello world')
    x='bangalore'
    print(x)
    #print(y)#y is not accessed because it is a local variable.
    def d2():#local scope.
        print('hello python learners')
        print(x)#x can be accessed bacause it is a global variable.
        y=200
        print(y)
    d2()
    print(x)
d1()


#nested function:
#it is one function taking inside another function.
#the main function is called outer function and the function
#which is inside the outer function is called inner function:
#nested function without arguments:
def d1():
    print('hello world')
    def d2():
        print('hello python learners')
    d2()
d1()
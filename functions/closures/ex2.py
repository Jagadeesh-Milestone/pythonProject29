#use of closure:
#even though the actual function is deleted we can use its functionality.
def d1():
    print('hello world')
    def d2(a,b):
        return 'hello python learners',a,b
    return d2(30,5)
d=d1()
print(d)
del d1
print(d)
print(d)
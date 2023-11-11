#print/return/yield:
def d1():
    print('hello world')
d1()
def d2():
    return 'hello python learners'
print(d2())
def d3():
    yield 'hello milestone'
d=d3()
print(next(d))

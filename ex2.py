def d1():
    def d2():
        return 'hello world'
    return d2()
d=d1()
print(d)

def d3():
    pass
d3()
def d4():
    print('hello world')
d4()



i=1
def d2():
    global i
    print('hello python learners',i)
    i+=1
    d2()
d2()
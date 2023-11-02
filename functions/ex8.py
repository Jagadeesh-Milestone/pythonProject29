#function as an argument value:
def d1(a):
    return 'd1 function',a
def d2():
    return 'd2 function'
d=d1(d2())
print(d)

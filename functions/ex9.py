#multiple functions
def d1(a,b):
    return 'd1 function',a,b
def d2(c):
    return 'd2 function',c
def d3():
    return 'd3 function'
d=d1(d2(d3()),d3())
print(d)

a=d2(d3())
print(a)
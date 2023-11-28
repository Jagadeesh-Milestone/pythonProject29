try:
    a=2
    b=4
    c=0
    print(a/b)
    print('statement one')
    print(b/c)
except ZeroDivisionError:
    print('statement two')
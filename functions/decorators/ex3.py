#nonlocal keyword:

def d1():
    l=[10,20,30,40]
    def d2():
        nonlocal l
        l.append(100)
        return l
    return d2
d=d1()
print(d())
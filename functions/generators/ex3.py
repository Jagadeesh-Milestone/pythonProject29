def  d2():
    yield 2000
    return 1000#we cant use return statement in generators.
    yield 3000
print(d2())
d=d2()
print(next(d))
print(next(d))
print(next(d))
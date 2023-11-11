#using for loop in generators:
def d3(n):
    for i in range(n):
        yield i
d=d3(3)
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))
for x in d3(10):
    print(x)

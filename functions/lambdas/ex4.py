#lambda function inside another function:
def d1(number):
    return lambda a,b:a*number+b
x=d1(10)
print(x(20,30))


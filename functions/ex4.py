#default argument value:
def d1(a,b=10):
    print(a+b)
d1(40)
d1(100,200)

def d2(country='India'):
    print('I am from',country)
d2('Sri lanka')
d2()
d2()
d2('australia')
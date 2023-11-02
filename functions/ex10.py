def d1(text):
    return text.upper()
def d2(text):
    return text.lower()
def d3(func):
    result=func('HellO WorLd')
    return result
d=d3(d1)
print(d)
d=d3(d2)
print(d)
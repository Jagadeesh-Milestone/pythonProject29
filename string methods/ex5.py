stringone='Hello! I have {:.3f} rupees'
x=stringone.format(10000)
print(x)

strigtwo='I have {:<10} mangos'
y=strigtwo.format(100)
print(y)

stringthree='I have {:>10} bananas'
z=stringthree.format(50)
print(z)

stringfour='I have {:^10} oranges '
a=stringfour.format(10)
print(a)

stringfive='I have {:,} dollars'
b=stringfive.format(10000000)
print(b)

stringsix='the binary format of {0} is {0:b}'
c=stringsix.format(10)
print(c)

stringseven='the decimal format of is {:d}'
d=stringseven.format(0b1010)
print(d)
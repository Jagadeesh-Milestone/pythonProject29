#data types:
#it is the type of the data which we are passing.
#python supports 6 types of data types.
#Number data types-int,float,complex,bin,hex,oct.
#sequences-list,tuple,range,string
#mapping-dict
#set-set,frozen set
#binary-bytes,bytearray
#booleans-True,False

#number data types:
#int:
#in python any real number will be treated as an integer value.
a=100
print(a)
print(type(a))

#float:
#in python any decimal numbers will be treated as a float value.
b=10.30
print(b)
print(type(b))

#complex numbers:
#the combination of a real number and an imaginary number is called
#complex number.
c=5-6j
print(c)
print(type(c))
print(c.imag)
print(c.real)

#binary numbers:
#they starts with 0b
#base value is 2
#possible values 0,1
a=10
print(bin(a))

b=0b1010
print(b)

#hexa decimal numbers:
#they starts with 0x
#base value is 16
#possible values are 0-9 and a-f
a=16
print(hex(a))

b=0xe
print(b)

#octal numbers:
#starts with 0o
#base value is 8
#possible values are 0-7
x=8
print(oct(x))

y=0o12
print(y)
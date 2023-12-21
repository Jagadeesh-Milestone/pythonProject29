z='jagadeesh'
#operators:
#operators are used to perform operations on variables and its
#values.
#python supports 7 types of operators.
#arithemetic operators
#assignment operators
#logical operators
#relational operators
#membership operators
#identity operators
#bitwise operators
#arithemetic operators.
#these are used to perform mathematical calculations.
a=10
b=5
print(a+b)#addition
print(a-b)#subraction
print(a*b)#multiplication
print(a/b)#division
print(a%b)#modulus
print(a//b)#floor divion
print(a**b)#power
print(z)
#assignment operators:
#these are used to assign the values:
c=10
c+=3
print(c)
c-=5
print(c)
c*=4
print(c)
c/=4
print(c)

#logical operators:
#logical and:
#it returns true if both statements are true otherwise it returns
# false.
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(z)
#logical or:
#it returns true if any one of the statements is true.
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#logical not
#it returns opposite to the given statement
print(not True)
print(not False)

#relational operators:
#these are used to compare two python objects.
print('relational operators')
a=5
b=10
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

#membership operators:
print('membership operators')
#these are used to check the membership of values in sequences.
#if it exists it returns true otherwise it returns false.
l=[10,20,30,'hello',True]
print(30 in l)
print('hello' in l)
print(100 in l)
print(30 not in l)
print('bangalore' not in l)

#identity operators:
print('identity operators')
#these are used to compare the ids of two python objects.
x=100
y=200
print(id(x))
print(id(y))
print(x is y)
print(x is not y)

l1=[10,20,30,40]
l2=[10,20,30,40]
l3=l1
print(id(l1))
print(id(l2))
print(id(l3))
print(l1 is l2)
print(l2 is l3)
print(l1 is l3)
print(l1 is not l2)
print(l2 is not l3)
print(l1 is not l3)

#bitwise operators:
#bitwise and
a=13
b=10
print(a&b)
print(bin(a))
print(bin(b))
print(bin(8))
#0b1101
#0b1010
#--------
#0b1000
#0b1111

#bitwise or
print(a|b)
print(bin(15))

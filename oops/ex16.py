#polymorphism:
#it is the property in which a single method having many forms.
#polymorphism in * operator:
#* is used for multiplication
a=10
b=20
print(a*b)

#* is used for power
c=5
d=4
print(c**d)

#* is used as arbitrary arguments
def d1(*students):
    print(students)
d1('hari','manoj','suresh')

#* is used to take keyword arguments in functions
def d2(**users):
    print(users)
d2(user1='manoj',user2='naresh')

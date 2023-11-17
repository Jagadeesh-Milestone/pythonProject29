a='10'
b='10.2'
c='hello'

#is decimal.
print(a.isdecimal())
print(b.isdecimal())
print(c.isdecimal())

#is digit:
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

#is numeric
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())

#is space:
#it returns true if a sting contains only spaces.
d="       "
print(d.isspace())
e=" hello"
print(e.isspace())

#strip:
#it is used to remove spaces in a string at beginning or ending.
f=" hello "
print(len(f))
print(f)
print(f.strip())
print(f.rstrip())
print(f.lstrip())

#justify:
g="hello"
print(g.rjust(20))
print(g.ljust(20))

#split:
x='hello python learners'
print(x.split())

y='hello,python,hello*java*learners'
print(y.split(','))

#replace:
#it is used to replace the characters of a string.
a='hello python hello java'
print(a.replace('l','mn'))
print(a.replace('l','jagadeesh',3))

#capitalize:
#first letter of the string will be in upper case remaining are in lower case
b="hello Python LearnerS"
print(b.capitalize())

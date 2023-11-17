#join:
x=['hello','python','lear','ners']
print('$'.join(x))

#starts with:
#it returns true if the string is strating with the given characters.
a="hello python learners"
print(a.startswith('hello'))

#ends with:
#it returns true if the string is ending with the given characters.
print(a.endswith('learners'))

#find:
#it is used to find the position of a character in a string.
b="hello bangalore"
print(b.find('o'))
print(b.find('l'))
print(b.rfind('l'))

#index:
c='hello python learners'
print(c.index('l'))
print(c.rindex('l'))

#new line:
d="hello python \n hello java"
print(d)

#tab space:
e="hello\t\t\tpython"
print(e)
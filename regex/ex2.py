#findall
import re

x='Hello Python Learners'
y=re.findall('[a-m]',x)
print(y)

a='I have 24 mangos and my mobile no is 87678690'
b=re.findall('\d',a)
print(b)

c='hello bangalore welcome to bangalore'
d=re.findall('ba.....re',c)
print(d)

#It checks whether the string is starting with the specified
#characters
d='hello python learners'
e=re.findall('^hello',d)
if e:
    print('string is starting with "hello"')
else:
    print('no match found')

#it checks whether the string is ending with the specified
#characters or not.
f='hello python hello java'
g=re.findall('java$',f)
if g:
    print('string is ending with "java"')
else:
    print('no match found')
#it checks whether a string containing a white space.
h='hello python'
i=re.findall('\s',h)
if i:
    print('there is a white space')
else:
    print('no whitespace')
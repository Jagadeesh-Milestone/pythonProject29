#search:
#it searches for all the possible matches
#if no match found None will be returned
import re
x='hello python learners'
y=re.search('\s',x)
if y:
    print('the first white space character is at',y.start())
else:
    print('no search found')

a='hello python'
b=re.search('l',a)
print(b)
#split:
#it will splits the string at match found:
import re
x='hello python learners'
y=re.split('l',x,2)
print(y)

#sub:
#it replaces the string with new charaters at each match:
a='hello java hello python'
b=re.sub('l','m',a,3)
print(b)
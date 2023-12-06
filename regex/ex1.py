#regular expressions:
#findall():
import re

x='hello python hello java'
y=re.findall('hello',x)
print(x)
#if there is a match it will be returned in a list
#if there is no match empty list will be returned
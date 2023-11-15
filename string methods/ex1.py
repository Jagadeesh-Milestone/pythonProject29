#string methods
s='bangalore'
print(len(s))
print(s.count('a'))
print(s[0])
print(s[::-1])

x='Hello woRlD'
print(x.upper())#all characters in upper case
print(x.lower())#all characters in lower case
print(x.title())#first character of every word is upper case
print(x.swapcase())#upper case to lower case and lower case to upper case

a="hello world"
print(a.islower())

b='HELLO WORLD'
print(b.isupper())

c='Hello World'
print(c.istitle())

d='pythonlearners'
print(d.isalpha())
#it returns true if a string contains only alphabets

e='python22learners'
print(e.isalnum())
#it returns true if a string contains both alphabets and numbers,
#only alphabets and only numbers but not others.




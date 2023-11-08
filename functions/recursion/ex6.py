#palindrome:
text=input('enter any text:')
x=reversed(text)
if list(text)==list(x):
    print(text,'is a palindrome')
else:
    print(text,'is not a palindrome')
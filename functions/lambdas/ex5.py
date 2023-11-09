#nested lambda:

x=lambda a:lambda b=20:a+b
y=x(10)
print(y())
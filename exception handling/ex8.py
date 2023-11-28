#raise an exception:
a='100'
if not type(a) is int:
    raise Exception('please enter only numbers')
else:
    print(a)


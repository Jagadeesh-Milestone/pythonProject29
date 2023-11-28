number=int(input('please enter any number:'))
if number not in range(1,100):
    raise Exception('please enter numbers between 1-99 only')
else:
    print(number)
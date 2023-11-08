#ebill:
print('\t \t welcome to BESCOM')
units=int(input('enter the no of units consumed:'))
if units<100 and units>0:
    print('no charges')
elif units>100 and units<150:
    print('ebill is:',units*2)
    print('pay ',units*2,' rupees to 9900990099')
elif units>150 and units<200:
    print('ebill is:',units*3)
    print('pay ',units*3,' rupees to 9900990099')
else:
    print('ebill is:',units*5)
    print('pay ',units*5,' rupees to 9900990099')


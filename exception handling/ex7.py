#finally:
#finally block will be excuted when we have exceptions and also
#when we dont have any exceptions
try:
    a=10
    b=5
    c=0
    print(a/c)
    print('statement one')
except Exception:
    print('statement two')
else:
    print('statement three')
finally:
    print('statement four')

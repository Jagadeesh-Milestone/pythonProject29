#else:
try:
    l=[10,20,30,40]
    print(l[7])
    print('statement one')
except Exception:
    print('statement two')
else:
    print('statement three')
#if there is an exception exception block will be executed.
#if there is no exceptions else block will be excuted.

#multiple expressions without lambda:
def d1(a,b,c,d):
    print(a+b)
    print(a-b)
    print(c*d)
    print(d/a)
d1(3,4,5,6)

#using lambda:
x=lambda s,t,u,v:(s+t,t-u,u*v,v/s)
print(x(2,3,4,5))
#numpy data types:
import numpy as np
x=np.array([10,20,30,40])
print(x.dtype)

y=np.array(['hari','manoj','bangalore','milestonetechnologies'])
print(y.dtype)

z=np.array([10.2,10.4,10.6])
print(z.dtype)

a=np.array([5+6j,6+8j])
print(a.dtype)

b=np.array([True,False,True])
print(b.dtype)

#converting one data type to other:
c=np.array([10.3,13.6,14.9],dtype=int)
print(c)

d=np.array([1,0,2,0,0,3,4,0],dtype=bool)
print(d)

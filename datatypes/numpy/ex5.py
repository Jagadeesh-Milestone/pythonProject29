#array shape. rows and columns
import numpy as np
x=np.array([10,20,30,40])
print(x)
print(x.shape)

y=np.array([[10,20,30],[40,50,60]])
print(y)
print(y.shape)

#reshape:
a=np.array([1,2,4,4,5,56,67,7])
print(a.reshape(2,4))

b=np.array([1,2,2,33,4,45,6,4,3,5])
print(b.reshape(5,2))
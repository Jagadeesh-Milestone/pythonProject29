#dimensions:
#dimension is the deapth of an array
#zero dimensional array:
import numpy as np
x=np.array((10))
print(x)
print(x.ndim)

#one-dimensional array
y=np.array([10,20,30,40])
print(y)
print(y.ndim)

#two-dimensional array
z=np.array([[10,20,30],[40,50,60]])
print(z)
print(z.ndim)

#three-dimensional array
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(a)
print(a.ndim)

#multi dimensional array:
b=np.array([10,20,30,40], ndmin=10)
print(b)
print(b.ndim)
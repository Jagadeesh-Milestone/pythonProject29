#accessing elements:
#we can access the elements of numpy array by using index position:
import  numpy as np

x=np.array([10,20,30,40])
print(x[0])
print(x[1]+x[3])
print(x[-3])

y=np.array([[10,20,30],[40,50,60]])
print(y[0])
print(y[0,0])
print(y[1,1])

z=np.array([[[1,2],[3,4]],[[4,6],[7,8]],[[9,10],[11,12]]])
print(z[0])
print(z[0,0])
print(z[0,0,0])
print(z[1])
print(z[1,1])
print(z[1,1,1])
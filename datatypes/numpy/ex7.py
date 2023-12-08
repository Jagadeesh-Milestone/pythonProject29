#copy and view.
import numpy as np
#in copy only original array will be affected
x=np.array([10,20,30,40])
y=x.copy()
x[0]=100
print(x)
print(y)
#in view both original array and copied array will be affected
z=x.view()
x[0]=200
print(x)
print(z)
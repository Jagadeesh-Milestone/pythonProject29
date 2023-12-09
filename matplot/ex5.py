#grid lines:
import  matplotlib.pyplot as mp
import numpy
x=numpy.array([2,4,6,8])
y=numpy.array([10,20,30,40])
mp.title('my graph')
mp.xlabel('x-axis')
mp.ylabel('y-axis')
mp.plot(x,y)
mp.grid()
mp.show()
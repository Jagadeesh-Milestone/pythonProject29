#ms-marker size
#mfc-marker face color
#mec-marker edge color
import matplotlib.pyplot as mp
import numpy
x=numpy.array([2,4,6,8])
y=numpy.array([1,3,5,7])
mp.plot(x,y,'o',ms=10,mfc='r',mec='g')
mp.show()

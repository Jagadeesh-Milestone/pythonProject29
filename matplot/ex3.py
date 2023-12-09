#marker,line and color
#syntax--marker|line|color
import matplotlib.pyplot as mp
import numpy
x=numpy.array([2,4,6,8])
y=numpy.array([5,6,7,8])
#mp.plot(x,y,'o:r')
#mp.plot(x,y,'*-g')
#mp.plot(x,y,'o:k')#black
#mp.plot(x,y,'s--b')
mp.plot(x,y,'o-.y')
mp.show()

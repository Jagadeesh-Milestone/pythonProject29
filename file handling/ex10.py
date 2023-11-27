#unpickling:
#it is the process of converting bye code to python object.
#we have to import pickle
#we use load method in unpickling.
import pickle
print('unpickling list')
f=open('html.dat','rb')
x=pickle.load(f)
print(x)
f.close()
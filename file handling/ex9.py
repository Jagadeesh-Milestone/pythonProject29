#pickling:
import pickle
print('pickling the list')
x=open('html.dat','wb')#write bytes
l=[10,20,30,40,50]
y=pickle.dump(l,x)
print(y)
x.close()

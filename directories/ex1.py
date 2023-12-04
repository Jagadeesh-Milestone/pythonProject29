#directories:
import os
#get current working directory
#x=os.getcwd()
#print(x)

#create new directory
#y=os.mkdir('python')
#print(y)
#we cant create two folders with same name

#create sub directory
#z=os.mkdir('python/oops')
#print(z)
#if the directory does not exists we cant create sub directory.

#rename directory:
#a=os.rename('java','html')
#print(a)

#rename subdirectory:
#b=os.rename('html/oops','html/functions')
#print(b)

#remove sub directory:
#c=os.rmdir('python/oops')
#print(c)
#we cant remove the main directory directly if there is a sub
#directory.first we have to remove sub directory and then main
#directory.

#remove directory
#d=os.rmdir('python')
#print(d)

print(dir(os))
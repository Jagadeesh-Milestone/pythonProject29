#file handling:
#creating and writing into a new file
f=open('hello.txt','w')#txt-text file,w-write
x=input('enter any text:')
y=f.write(x)
f.close()

#while loop in file handling:
f=open('python.txt','w')
course='python'
while course=='python':
    course=input('enter the course:')
    f.write(course)
    print(course)
f.close()

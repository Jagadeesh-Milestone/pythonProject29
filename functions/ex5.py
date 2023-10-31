#arbitary arguments *args:
#if you dont know how many values you are passing then put a *
#before the argument name:
def d1(*students):
    print(students)
    print('tallest student is',students[0])
d1('hari','manoj','suresh','naresh')

#keyword arguments (**kwargs):
#we can pass the values to the keywords:
def d2(**users):
    print(users)
    print('shortest student is',users['user3'])
d2(user1='jagadeesh',user2='suresh',user3='hari')
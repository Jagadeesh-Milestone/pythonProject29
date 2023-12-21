#nested if:
#it is used to take one if statement inside another if statement.
a=50
if a<60:
    print('first condition is true')
    if a<30:
        print('second condition is true')
    else:
        print('second condition is false')
        if a>40:
            print('third condition is true')
            if a==50:
                print('fourth condition is true')
                if a!=50:
                    print('fifth condition is true')
                else:
                    print('fifth condition is false')
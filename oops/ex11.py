#inheritance:
#It is the property in which one class is accessing all the attributes
#and methods of another class is called inheritance.
#here the class which is accessing is called child/derived/subclass.
#the class from where another class is being inheriting is called
#parent/base/super class.
#there are five types of inheritance in python.
#single level inheritance.
#multi level inheritance.
#multiple inheritance.
#hirerarcheal inheritance.
#hybrid inheritance.

#single level inheritance.
#it is the property in which a single child class deriving from a
#single parent class.
class parent:
    parentmoney=30000
    def d1(self):
        print('i am parent property')

class child(parent):
    money=20000
    def d2(self):
        print('i am child property')
c=child()
print(c.parentmoney)
print(c.money)
c.d1()
c.d2()


#__init__ method:
class milestone:
    def __init__(self,name,location):
        self.name=name
    def d1(self,address):
        print('welcome',self.name)
        print(address)
    def d2(self):
        print('hello',self.name)
obj1=milestone('jagadeesh')
obj1.d1()
obj1.d2()

obj2=milestone('hari')
obj2.d1()
obj2.d2()

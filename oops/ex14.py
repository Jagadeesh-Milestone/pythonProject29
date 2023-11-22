#hirerarcheal inheritance:
#it is the property in which more than one child classes deriving
#from a single parent class.
class grandparent:
    gmoney=10000
    def d1(self):
        print('im grandparent property')
class parent(grandparent):
    pmoney=20000
    def d2(self):
        print('im parent property')
class child(grandparent):
    cmoney=30000
    def d3(self):
        print('im child property')
c=child()
print(c.gmoney)
print(c.cmoney)
c.d1()
c.d3()

p=parent()
print(p.gmoney)
print(p.pmoney)
p.d1()
p.d2()

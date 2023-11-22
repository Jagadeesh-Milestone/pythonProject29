#hybrid inheritance:
#it is the combination of more than one type of inheritances.
class grandparent:
    gmoney=20000
    def d1(self):
        print('im grandparent property')
class parent(grandparent):
    pmoney=30000
    def d2(self):
        print('im parent property')
class child(parent,grandparent):
    cmoney=10000
    def d3(self):
        print('im child property')
c=child()
print(c.gmoney)
print(c.pmoney)
print(c.cmoney)
c.d1()
c.d2()
c.d3()

p=parent()
print(p.gmoney)
print(p.pmoney)
p.d1()
p.d2()

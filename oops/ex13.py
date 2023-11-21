#multiple inheritance:
class grandparent:
    gmoney=10000
    def d1(self):
        print('grandparent property')
class parent:
    pmoney=20000
    def d2(self):
        print('parent property')
class child(grandparent,parent):
    cmoney=30000
    def d3(self):
        print('child property')
c=child()
print(c.gmoney)
print(c.pmoney)
print(c.cmoney)
c.d1()
c.d2()
c.d3()

p=parent()
print(p.pmoney)
p.d2()
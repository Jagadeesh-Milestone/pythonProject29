#multi level inheritance:
class grandparent:
    gmoney=20000
    def d1(self):
        print('i am grandparent property')
class parent(grandparent):
    pmoney=30000
    def d2(self):
        print('i am parent property')
class child(parent):
    cmoney=10000
    def d3(self):
        print('i am child property')
c=child()
print(c.gmoney)
print(c.pmoney)
print(c.cmoney)
c.d1()
c.d2()
c.d3()

#method overloading:
class milestone:
    def d1(self,a,b):
        print(a+b)
    def d1(self,a,b,c):
        print(a+b+c)
m=milestone()
m.d1(10,20)

#encapsulation:
class python:
    def d1(self):
        self._a=200
class java(python):
    def d2(self):
        python.d1(self)
        print('parent class attribute',self._a)
        a=100
        print('child class attribute',a)
j=java()
j.d1()
j.d2()


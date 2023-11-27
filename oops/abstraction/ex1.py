#abstraction:
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        print('polygon has many sides')
class triangle(polygon):
    def sides(self):
        print('triangle has three sides')
class square(polygon):
    def sides(self):
        print('square has four sides')
class pentagon(polygon):
    def sides(self):
        print('pentagon has five sides')
p=pentagon()
p.sides()

s=square()
s.sides()

t=triangle()
t.sides()

p=polygon()
p.sides()
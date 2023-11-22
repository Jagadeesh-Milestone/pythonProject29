#polymorphism in oops:
class bird:
    def fly(self):
        print('some birds can fly and some cannot fly')
class eagle(bird):
    def fly(self):
        print('an eagle can fly at very heights')
class parrot(bird):
    def fly(self):
        print('a parrot can fly but not at very heights')
class ostrich(bird):
    def fly(self):
        print('an ostrich cannot fly')
b=bird()
b.fly()
o=ostrich()
o.fly()
p=parrot()
p.fly()
e=eagle()
e.fly()
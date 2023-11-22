class vehicle:
    def transport(self):
        print('vehicle are used to travel')
class car(vehicle):
    def transport(self):
        print('car is used to travel on roads')
class aeroplane(vehicle):
    def transport(self):
        print('aeroplane is used to travel on air')
class ship(vehicle):
    def transport(self):
        print('ship is used to travel on water')
v=vehicle()
v.transport()
s=ship()
s.transport()
a=aeroplane()
a.transport()
c=car()
c.transport()
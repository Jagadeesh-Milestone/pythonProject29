#class/instance/static
class milestone:
    course='python'
    def d1(self):
        name='jagadeesh'
        print('im taking',milestone.course,'my name is',name)
    @classmethod
    def d2(cls):
        name='hari'
        print('im taking',cls.course,'my name is',name)
    @staticmethod
    def d3():
        name='manoj'
        print('im taking',milestone.course,'my name is',name)
obj1=milestone()
obj1.d1()

obj2=milestone
obj2.d2()

obj3=milestone
milestone.d3()
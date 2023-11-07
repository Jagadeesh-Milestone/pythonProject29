#finding the recursion limit:
import sys
print(sys.getrecursionlimit())
x=sys.setrecursionlimit(1400)
print(x)
print(sys.getrecursionlimit())
x=1
def d3():
    global x
    print('d3 function',x)
    x+=1
    d3()
d3()

#electricity bill:
#name:
#input (units)
#units <100 no charges
#units >100 and <150  2/unit
#unts >150 and <200 3/units
#pay your bill 300 to 6305134256







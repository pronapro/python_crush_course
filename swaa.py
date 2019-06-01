def swap(x,y):
    print("X ",x)
    print("Y ",y)
    hold =  x
    x = y
    y =hold
    print("new X ",x)
    print("new y ",y)
swap(9,43)
def pyswap(x,y):
    print("X ",x)
    print("Y ",y)
    x,y = y,x
    print("new X ",x)
    print("new y ",y)

pyswap(5,7)

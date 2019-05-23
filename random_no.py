from random import randint
def random():
    for i in range (50):
        x = randint(3,6)
        print(x)
#random()

def random_x_y():
    x = randint(1,50)
    y =randint(2,5)
    comput = x**y
    print("x"+ " "+ str(x))
    print("y"+ " "+ str(y))
    print("answer is" + " "+str(comput) )
random_x_y()

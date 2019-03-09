import random
for i in range(10):
    print(random.random())
print()
#make it custome
#scaling by 4
for i in range(20):
    print(4*random.random())
print()
for i in range(10):
    print(4*random.random()+3)
#bell curve normal distribution
#it uses mean and standard deviation
print("normal distribution")
for i in range(10):
    print(random.normalvariate(0,2))
    #discrete distribution like a dice roll
print("discrete probability")
for i in range(20):
    print(random.randint(1,6))
#picking from a list of numbers
print("not numbers")
direction =["N","E","S","W"]
for i in range(10):
    print(random.choice(direction))

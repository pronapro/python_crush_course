def num_square(n):
    for i in range(1,n+1):
        square = i**2
        print(str(i) + "---" +str(square))
n = int(input())
num_square(n)

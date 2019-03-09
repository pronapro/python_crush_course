#lambda expression
d =lambda x:x**3
print(d(3))
#map
A =[4,6,8,9,23,54,67,78]
B = list(map(lambda x:x**3,A))
print(B)

#filter function
#used depending on a given condition
C = list(filter(lambda x:x%2 !=0,A))
print(C)

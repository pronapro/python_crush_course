count = 0
end_1 = []
for i in range(1,101):
    if (i**2)%10 ==1:
        count = count+1
        end_1.append(i**2)
print(count)
print(end_1)

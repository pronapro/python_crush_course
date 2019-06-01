def count_even(N):
    even_no = 0
    odd_no = 0
    even_list = []
    odd_list =[]
    for i in range(N):
        if i%2 ==0:
            even_no = even_no+1
            even_list.append(i)
        else:
            odd_no = odd_no+1
            odd_list.append(i)
    print("even",even_no)
    print("odd", odd_no)
    print(even_list)
    print(odd_list)
count_even(23)

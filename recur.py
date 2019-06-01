def recur(n):
    if n <= 1:
        return 1

    ansa =n+recur(n-1)
    print(ansa)
recur(2)

def prime_Num(N):
	primes = []
	for possible_num in range(2,N):
		is_prime =True
		for num in range(2,possible_num):
			if possible_num%num == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(possible_num)
	print(primes)
n = int(input())
prime_Num(n)	
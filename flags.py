def flag_demo():
	Leave = False
	count = 0
	while(count<10):
		if count ==5 and Leave ==False:
			hello()
			Leave =True
		count += 1
	print(Leave)
def hello():
	print("hello there")
flag_demo()
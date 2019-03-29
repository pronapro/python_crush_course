def swap():
	X =4
	Y = 7

	#swapping variables
	#use a temporaly holder Temp
	temp = X
	X= Y
	Y = temp

	return X,Y
print(swap())

import random

def rng(min,max):
	return random.randint(min,max)

def jersey_number():
	return rng(1,100000)

def jersey_size():
	number = rng(1,5)

	# Jersey Size
	if number == 1:
		size = "M"
	elif number == 2:
		size = "L"
	elif number == 3:
		size = "XL"
	elif number == 4:
		size = "XXL"
	else:
		size = "XXXL"

	return size

def jersey_color():
	coin = rng(1,2)

	# Jersey Color	
	if coin == 1:
		color = "Black"
	else:
		color = "White"

	return color
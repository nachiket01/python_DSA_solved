number = int(input())
number1 = 0 
number2 = 0

while number1 or number2 == 0:

	number1 = number // 10
	number2 = number % 10

	if number1 == 0:
		print(number2)
		break

	elif number2 == 0:
		print(number1)
		break

	else:
		number = number1**2 + number2**2
		#print(number)

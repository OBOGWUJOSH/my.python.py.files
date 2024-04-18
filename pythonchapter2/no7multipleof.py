#no7multipleof.py

numerator = int(input('Enter a number to determine the factor: '))
denominator = int(input('enter a factor: '))

factor_calculator = (numerator%denominator)

if factor_calculator > 0:
	
	print(denominator, 'Is not a factor of', numerator)

else: 

	print(denominator, 'is a factor of', numerator)	
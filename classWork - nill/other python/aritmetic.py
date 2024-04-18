number1 = (float(input("enter number: ")))
number2 = (float(input("enter number: ")))

print(type(number1))

devi= (number1 / number2)
add = (number1 + number2)
sub = (number1 - number2)
multi = (number1 * number2)
fldev = (number1 // number2)
expo = (number1 ** number2)
squ = (expo ** 0.5)

devision = "the devision of " + str(number1) + " and " + str(number2) + " is " + str(devi)
subtraction = "the subtraction of " + str(number1) + " from " +str(number2) + " is " + str(sub)
addition = "the addition of " + str(number1) + " and " + str(number2) + " is " + str(add)
multiplication = str(number1) + " multiplied " + " by " + str(number2) + " is " + str(multi)
exponential = expo
squareroot = squ
floor_devision = fldev

print(devision)	
print(subtraction)		
print(addition)
print(multiplication)
print(exponential)
print(squareroot)
print(floor_devision)
#numberGameWithRandom
import random

random = random.randrange(1,10)

print(random)

number = 0

while number != random:
	number = (int(input("enter a number from 1 to 10:")))

	if number !=random:
		print("wrong number try again")

	else :
		number == random

		print("congratulation you have won")

		break;


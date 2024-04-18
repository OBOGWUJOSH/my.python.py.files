# sum task 1 (sum of loops)

add = 0
sum = 0
multiple_sum = 0
x = 0

for x in range (20001):
	if x%10 == 0:
		sum += x + multiple_sum;
print("The sum of all the multiples of 10 from 1 to 20000 is", sum)

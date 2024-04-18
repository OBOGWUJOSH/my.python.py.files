# sum task 3 (sum of loops)

add = 0
number = 3
multiple_sum = 0
multiple_of_three = 0
i = 2


for i in range (1,100):
	if i%2 == 0:
		i = multiple_sum + i
		print(i, end=" ")
		#print("The even numbers between one and hundred are"i, end=" ")

		
#sumtask4
pass_mark = 45
pass_mark_count = 0
scores_over_45 = 0
scores_below_44 = 0
score_count = 0

for x in range (15):

	scores = int(input('enter students score over 100 :'))

	if scores > 100:
		print('you are a scam')

	if scores >= 45:

		scores_over_45 += score_count + 1
		print('HURRAY!!!!! YOU PASSED YOUR FINAL EXAM !!!!!!')

	elif scores <= 44:
		scores_below_44 += score_count + 1
		print('***you failed repeat your exam next year***')


print('passed:',scores_over_45)
print('failed',scores_below_44)




	


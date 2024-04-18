#passedandfailed.py



students_name = (input('Enter the students name:  '))
students_score = int(input('Enter the students score: '))
STUDENT_PASS_MARK = 45


if students_score >= 45 <= 100:
	print('CONGRATULATIONS', students_name )
	print('your score is', students_score)
	print('YOU HAVE PASSED!!!' )


if students_score < 45:
	print('i am sorry', students_name )
	print('your score is', students_score)
	print('YOU HAVE FAILED' )
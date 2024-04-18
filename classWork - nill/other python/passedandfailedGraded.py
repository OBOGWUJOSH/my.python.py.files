#passedandfailedGraded.py
#your score is this your grade is this


students_name = (input('Enter the students name:  '))
students_score = int(input('Enter the students score: '))



if students_score > 100:
	print (students_name,'you are a fraud')
elif students_score >=80 and students_score <= 100:
	print (students_name, 'Your score is', students_score , 'your grade is A')
elif students_score >= 66 and students_score < 80:
	print (students_name, 'Your score is', students_score, 'your grade is B')
elif students_score >= 51 and students_score <= 65:
	print (students_name, 'Your score is', students_score, 'your grade is C')
elif students_score > 40 and students_score > 50:
	print (students_name, 'Your score is', students_score, 'your grade is D')
else:
	print (students_name, 'you are a faliure')










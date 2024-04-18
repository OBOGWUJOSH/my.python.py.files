#***weather_condition_code.py"""
temprature = float(input("Enter the tempature: "))

if temprature >= 70:
	print ('o gbona feli feli')
elif temprature > 40 and temprature< 70:
	print('The weather is hot')
elif temprature > 20 and temprature <= 40:
	print('The weather is average')
elif temprature >=1 and temprature <=20:
	print('the weather is cold')
	print('Go out With your sweater')
else:
	print('The weather is extremely cold')
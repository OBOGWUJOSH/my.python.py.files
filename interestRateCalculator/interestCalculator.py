amount = (int(input("amount invested:")))

rate = (int(input("enter yearly interst rate %:" )))
	
years = (int(input("amount of years:" )))


count = 0




for year in range (1,years):
	
	interest_calculation = (rate / 100.0) * amount
	

	amount = interest_calculation + amount


	count+= 1


	print("The interest calculated for year", count, "is", amount)


#pymyestore.py
print('welcome to the box')
user_name = input("Enter customers name:" )
print('welcome ' + user_name)
items_bought = int(input("number of item purchased:" ))
counter = 0
total = 0
price_of_item = 0
percentage_discount = float(input("percentage discount:" ))

while counter < items_bought:
	
	price_of_item = int(input("price of item ", counter, ": "))
	total += price_of_item
	counter += 1
print(total)


percentage_calculation = total * (percentage_discount/100) 
print(percentage_calculation)


discounted_price = total - percentage_calculation

print(discounted_price)



	
	
	



	

	
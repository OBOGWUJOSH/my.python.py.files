price = (int(input('input the price of product: ')))
percentage = (int(input('input the percent: ')))

percentage_maths = (price * percentage)/100

discount_price = (price - percentage_maths)

print(discount_price)
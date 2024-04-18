#mortgage name / principal amount/ anual interest rate/ duration for mortgage payment

print("welcome to heritage mortgage")

name = (input("Enter your name:  "))

print("welcome to heritage mortgage service", name)

number = 1

Annual_interest_rate = float(input('input the annual interest rate:'))
principal_amount = (int(input('input principal amount:#' )))
Duration_for_of_the_loan = (int(input('duraion for the loan in years:')))




up_maths = ((Annual_interest_rate/100)/12) * (number + Annual_interest_rate/100)/12)) ** (Duration_for_of_the_loan/12)

down_maths = ((number + (Annual_interest_rate/100)/12) ** (Duration_for_of_the_loan*12))-1


mortgage_maths = principal_amount*(up_maths/down_maths)

print(mortgage_maths)
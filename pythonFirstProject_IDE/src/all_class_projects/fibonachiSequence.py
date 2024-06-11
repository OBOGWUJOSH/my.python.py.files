initial_Number: int = 0
initial_Number1: int = 1
addedNumbers:  int = initial_Number

for numbers in range(11):
    print(addedNumbers,end  = " ")
    initial_Number, initial_Number1 = initial_Number1 , addedNumbers
    addedNumbers = initial_Number + initial_Number1


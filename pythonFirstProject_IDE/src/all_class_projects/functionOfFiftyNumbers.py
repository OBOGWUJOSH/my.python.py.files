def isEven(listOfNumbers):
    even_number_list = []
    for input_of_number in listOfNumbers:
        if input_of_number % 2 == 0:
            even_number_list.append(input_of_number)
    return even_number_list

def isOdd(listOfNumbers2):
    odd_number_list = []
    for input_of_number in listOfNumbers2:
        if input_of_number % 2 == 1:
            odd_number_list.append(input_of_number)
    return odd_number_list


# def isMultiplied(listOfNumbers3):
#     odd_number_list = []
#     for input_of_number in listOfNumbers3:
#         if input_of_number % 2 == 1:
#             odd_number_list.append(input_of_number)
#     return odd_number_list




# numberz = list(range(0,100))
# print(isEven(numberz))
#
#
# numberz = list(range(0,100))
# print(isOdd(numberz))


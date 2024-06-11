import random

random.seed(49)


def ten_number_generator():
    numbers = []
    for number in range(10):
        random_number = random.randint(0, 50)
        numbers.append(random_number)
    return numbers


#print(ten_number_generator())

new_numbers = ten_number_generator()


#print(new_numbers)


def length_of_list(new_numbers):
    count = 0
    for number in new_numbers:
        if number > 0:
            count += 1
    return count


new_numbers = ten_number_generator()


#print(length_of_list(new_numbers))
#print(new_numbers)


def sum_up_even_index(new_numbers):
    sum_up = 0
    for i in range(length_of_list(new_numbers)):
        if i % 2 == 0:
            sum_up += new_numbers[i]
    return sum_up


#print(sum_up_even_index(new_numbers))
#print(new_numbers)


def sum_up_odd_index(new_numbers):
    sum_up = 0
    for i in range(length_of_list(new_numbers)):
        if i % 2 == 1:
            sum_up += new_numbers[i]
    return sum_up


#print(sum_up_odd_index(new_numbers))
#print(new_numbers)


def multiply_third_element(new_numbers):
    multiply_up = 1
    for count in range(0, length_of_list(new_numbers), 3):
        multiply_up *= new_numbers[count]
    return multiply_up


#print(multiply_third_element(new_numbers))
#print(new_numbers)


def average_of_all_element(new_numbers):
    summUp = 0
    average = 0
    for count in range(length_of_list(new_numbers)):
        summUp += new_numbers[count]
        average = summUp / length_of_list(new_numbers)
    return average


#print(average_of_all_element(new_numbers))
#print(new_numbers)


def largest_element(new_numbers):
    temp_largest_number = 1
    for element in new_numbers:
        if element >= temp_largest_number:
            temp_largest_number = element
    return temp_largest_number


#print(largest_element(new_numbers))
#print(new_numbers)


def smallest_element(new_numbers):
    temp_smallest_number = new_numbers[1]
    for element in new_numbers:
        if element <= temp_smallest_number:
            temp_smallest_number = element
    return temp_smallest_number


new_string_list = ["jesus", "james", "john", "jane", "justin", "estate", "1000001"]


def number_of_string(new_string_list):
    new_chars_list = []
    counter = 0
    lengthOfString = len(new_string_list)
    for string in new_string_list:
        if lengthOfString >= 2 and (string[0] == string[-1]):
            counter += 1
            new_chars_list.append(string[0])
    return counter, new_chars_list


#print(number_of_string(new_string_list))

#
# for number in range(1, 16):
#     numbers_list = []
#     numbers_list = number
#
#     print(numbers_list, end=" ");

for number in range(1, 16):
    numbers_list = []
    #numbers_list = number
    new_copied_list  = numbers_list.copy()
    print(new_copied_list)

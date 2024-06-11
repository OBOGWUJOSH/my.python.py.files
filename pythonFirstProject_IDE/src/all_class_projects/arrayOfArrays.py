from typing import List

sub_list = []
main_list = []
# subList2 = [0, 1, 2, 3, 4]
# subList3 = [0, 1, 2, 3, 4]
#mainList = [subList0, subList1, subList2, subList3]

for number in range(4):
    sub_list = []
    for number2 in range(5):
        sub_list.append(number * number2)
        main_list.append(sub_list)

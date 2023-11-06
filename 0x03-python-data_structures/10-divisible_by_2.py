#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_list = []
    for i in my_list:
        check_list.append(True if i % 2 == 0 else False)

    return check_list

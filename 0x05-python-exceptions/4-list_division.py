#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except:
            new_list.append(0)
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif my_list_2[i] == 0:
                print("division by 0")
            elif not my_list_2[i].isdigit():
                print("wrong type")
        finally:
            continue

    return new_list

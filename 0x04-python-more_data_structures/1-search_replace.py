#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        new_list.append(replace if item == search else item)

    return new_list

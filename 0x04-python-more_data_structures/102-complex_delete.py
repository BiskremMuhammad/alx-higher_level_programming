#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = ""
    for i in a_dictionary:
        if a_dictionary[i] == value:
            del a_dictionary[i]

    return a_dictionary

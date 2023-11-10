#!/usr/bin/python3
def best_score(a_dictionary):
    max_value_key = None
    max_value = 0
    for k in a_dictionary:
        if a_dictionary[k] > max_value:
            max_value_key = k
            max_value = a_dictionary[k]

    return max_value_key

#!/usr/bin/python3
def common_elements(set_1, set_2):
    shortest = set_1 if len(set_1) < len(set_2) else set_2
    longest = set_1 if len(set_1) >= len(set_2) else set_2
    duplicates = []
    for item in shortest:
        if item in longest:
            duplicates.append(item)

    return duplicates

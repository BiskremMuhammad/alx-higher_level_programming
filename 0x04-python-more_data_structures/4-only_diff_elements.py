#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    shortest = set_1 if len(set_1) < len(set_2) else set_2
    longest = set_1 if len(set_1) >= len(set_2) else set_2
    duplicates = []
    differences = []
    for item in shortest:
        if item in longest:
            duplicates.append(item)

    union = list(set(set_1, set_2))
    for item in union:
        if not item in duplicates:
            differences.append(item)

    return differences

#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    different = []

    for value in set_1:
        if value not in set_2:
            different.append(value)
    for value2 in set_2:
        if value2 not in set_1:
            different.append(value2)
    return set(different)

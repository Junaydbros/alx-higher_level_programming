#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for integer in my_list:
        if idx < 0:
            pass
        if idx > len(my_list):
            pass
        element[idx] = integer

#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    org_list = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return org_list

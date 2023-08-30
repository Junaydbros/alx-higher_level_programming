#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    org_list = my_list.copy()
    if idx < 0:
        return org_list
    if idx >= len(my_list):
        return org_list
    org_list[idx] = element
    return org_list

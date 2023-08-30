#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == [] or my_list is None:
        return
    for integer in list(reversed(my_list)):
        print("{:d}".format(integer))

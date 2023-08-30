#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for integer in list(reverse(my_list)):
        print("{:d}".format(integer))

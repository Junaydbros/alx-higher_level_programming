#!/usr/bin/python3

def no_c(my_string):
    if 'c' is in my_string:
        my_string.remove('c')
    if 'C' is in my_string:
        my_string.remove('C')
    return my_string

#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest = my_list[0]
    for anInt in my_list:
        if anInt > largest:
            largest = anInt
    return largest

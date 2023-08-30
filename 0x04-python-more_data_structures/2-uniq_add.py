#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniqueList = list(set(my_list))

    for value in uniqueList:
        sum = sum + value
    return sum

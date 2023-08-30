#!/usr/bin/python3

def complex_delete(dictionary, value):
    deletableKeys = [key for key, digit in a_dictionary.items() if digit == value]

    for key in deletableKeys:
        del a_dictionary[key]
    return a_dictionary

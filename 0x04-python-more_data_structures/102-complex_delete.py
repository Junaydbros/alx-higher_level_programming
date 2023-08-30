#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deletableKeys = [key for key, param in a_dictionary.items() if param == value]

    for key in deletableKeys:
        del a_dictionary[key]
    return a_dictionary

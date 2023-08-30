#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newDictionary = {}
    for param in a_dictionary:
        newDictionary[param] = a_dictionary[param] * 2
    return newDictionary

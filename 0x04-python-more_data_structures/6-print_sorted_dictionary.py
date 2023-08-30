#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedDictionary = sorted(a_dictionary.items())

    for param in sortedDictionary:
        print(f"{param[0]}: {param[1]}")

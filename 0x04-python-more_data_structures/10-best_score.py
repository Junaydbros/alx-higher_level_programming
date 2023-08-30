#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    largest = max(a_dictionary.value())
    for param in a_dictionary:
        if a_dictionary[param] == largest:
            return param
    return None

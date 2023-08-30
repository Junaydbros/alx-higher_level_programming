#!/usr/bin/python3

def no_c(my_string):
    newStr = ""
    for ch in range(len(my_string)):
        if my_string[ch] != 'C' and my_string[ch] != 'c':
            newStr += my_string[ch]
    return newStr

#!/usr/bin/python3

def print_last_digit(number):
    convNumber = str(number)
    print("{}".format(int(convNumber[-1])), end="")
    return convNumber[-1]

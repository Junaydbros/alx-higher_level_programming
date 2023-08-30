#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    prevValue = 0

    for numeral in roman_string:
        number = roman[numeral]
        if number > prevValue:
            value += number - 2 * prevValue
        else:
            value = value + number

        prevValue = number

    return value

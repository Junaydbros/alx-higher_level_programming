#!/usr/bin/python3

def remove_char_at(str, n):
    newStr = ""
    for idx, value in enumerate(str):
        if idx == n:
            continue
        newStr = newStr + value
    return newStr

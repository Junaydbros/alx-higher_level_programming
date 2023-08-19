#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if (ord(ch) >= 97 and ord(ch) <= 122):
            strInCaps = ord(ch) - 32

        print("{}".format(chr(strInCaps)), end="")
    print()

#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if not ('A' <= str <= 'Z'):
            try:
                strInCaps = ord(ch) - 32
            #print("{}".format(chr(strInCaps)), end="")
            except ('A' <= str <= 'Z'):
                #strInCaps = ord(ch)
                pass
            print("{}".format(chr(strInCaps)), end="")
        else:
            return str
    #print("{}".format(chr(strInCaps)), end="")
    print()

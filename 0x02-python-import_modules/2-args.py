#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    print("{} arguments".format(len(argv)), end="")

    if len(argv) == 1:
        print(".")
    elif len(argv) > 1:
        print(": ")

    #arg = sys.argv[1:]
    for i, arg in enumerate(argv):
        print("{}: ".format((i + 1), arg))

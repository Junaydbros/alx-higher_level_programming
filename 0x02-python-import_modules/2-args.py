#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":

    print("{} arguments".format(len(argv)), end="")

    if len(argv) == 0:
        print(".")
    elif len(argv) > 0:
        print(": ")

    arg = sys.argv[1:]
    for i, arg in enumerate(argv):
        print("{}: ".format((i + 1), arg))

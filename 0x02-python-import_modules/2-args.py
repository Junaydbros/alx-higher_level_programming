#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":

    print("{} ".format(len(argv) - 1), end="")

    if len(argv) == 1:
        print("arguments.")
    elif len(argv) > 2:
        print("arguments:")
    else:
        print("argument:")

    for i in range(1, len(argv)):
        print("{}: ".format(i, argv[i]))

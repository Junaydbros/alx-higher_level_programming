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

    #arg = sys.argv[1:]
    for i in range(len(argv)):
        print("{}: ".format((i + 1), argv[i]))

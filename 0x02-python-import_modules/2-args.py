#!/usr/bin/python3

if __name__ == "__main__":

    print("{} arguments".format(len(argv)), end="")

    if len(argv) == 0:
        print(".")
    elif len(argv) > 0:
        print(": ")

    for i, arg in enumerate(argv):
        print("{}: ".format((i + 1), arg))

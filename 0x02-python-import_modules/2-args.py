#!/usr/bin/python3

if __name__ == "__main__":

    print("{} arguments".format(len(argv)), end="")

    for i, arg in enumerate(argv):
        if len(argv) == 0:
            print(".")
        elif len(argv) > 0:
            print(": ")

        print("{}: ".format(i + 1), arg)

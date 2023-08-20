#!/usr/bin/python3

import sys
#if __name__ == "__main__":

    def argPrinter(*argv):
        print("{} arguments".format(len(argv)), end="")

        if len(argv) == 0:
            print(".")
        elif len(argv) > 0:
            print(": ")

        for i, arg in enumerate(argv):
            print("{}: ".format((i + 1), arg))

if __name__ == "__main__":
    arg = sys.args[1:]
    argPrinter(*arg)

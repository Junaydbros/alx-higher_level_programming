#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    print("{} ".format(len(argv) - 1), end="")

    if len(argv) == 1:
        print("arguments.")
    elif len(argv) > 2:
        print("arguments: ")
    else:
        print("argument: ")

    #arg = sys.argv[1:]
    for i, arg in enumerate(argv):
        print("{}: ".format((i + 1), arg))

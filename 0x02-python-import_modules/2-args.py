#!/usr/bin/python3

if __name__ == "__main__":
    print("{} arguments:".format(len(argv)))

    if len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    for i in argv:
        print("{}: ".format(i), argv[i])

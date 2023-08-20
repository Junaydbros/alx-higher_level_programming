#!/usr/bin/python3

from sys import argv

if __name__ = "__main__":
    sum = 0
    for cnt in range(1, len(argv)):
        sum += int(argv[cnt])
    print(sum)

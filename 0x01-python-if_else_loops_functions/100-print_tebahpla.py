#!/usr/bin/python3

cnt = 0
for ch in reversed(range(ord('a'), ord('z') + 1)):
    cnt = cnt + 1
    if (cnt % 2) == 0:
        res = -32
    else:
        res = 0
    print("{}".format(chr(ch + res)), end="")

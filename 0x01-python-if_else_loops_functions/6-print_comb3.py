#!/usr/bin/python3
for numb in range(0, 9):
    for pvalue in range(numb + 1, 10):
        print("{}{}".format((numb % 10), (pvalue % 10)), end="")

        if numb == 8 and pvalue == 9:
            continue
        print(", ", end="")
print("\n", end="")

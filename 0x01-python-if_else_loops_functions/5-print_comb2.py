#!/usr/bin/python3
for num in range(0, 10):
    for pvalue in range(0, 10):
        print("{}{}, ".format(num, pvalue), end="")

        if num + pvalue == 18:
            print("{}{}".format(num, pvalue))
        else:
            continue

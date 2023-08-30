#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            cnt++
        except (ValueError, TypeError):
            pass
        print()
        return cnt

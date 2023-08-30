#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        cnt = 0
        for b in matrix[a]:
            print("{:d}".format(b), end="")
            if cnt < len(matrix[a]) - 1:
                print(" ", end="")
            cnt = cnt + 1
        print()

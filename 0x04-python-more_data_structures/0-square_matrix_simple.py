#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrixStorer = []
    for value in range(len(matrix)):
        matrixStorer.append(list(map(lambda a: a**2, matrix[value])))
    return matrixStorer

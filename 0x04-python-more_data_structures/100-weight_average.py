#!/usr/bin/python3

def weight_average(my_list=[]):
    nom = 0
    denom = 0

    if not my_list:
        return 0
    for value in my_list:
        nom = nom + value[0] * value[1]
        denom = denom + value[1]
    return nom / denom

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    answer = []

    for numb in my_list:
        if numb % 2 == 0:
            answer.append(True)
        else:
            answer.append(False)
    return answer

#!/usr/bin/python3

def common_elements(set_1, set_2):
    theCommon = []
    for value in set_1:
        if value not in set_2:
            continue
        else:
            theCommon.append(value)
    return set(theCommon)

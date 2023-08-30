#!/usr/bin/python3

def search_replace(my_list, search, replace):
    storeList = []

    if len(my_list) == 0:
        return storeList
    for value in my_list:
        if value == search:
            storeList.append(replace)
        else:
            storeList.append(value)
    return storeList

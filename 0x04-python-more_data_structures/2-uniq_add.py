#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    else:
        new_list = list(set(my_list))
        result = 0
        for item in new_list:
            result += item
        return result

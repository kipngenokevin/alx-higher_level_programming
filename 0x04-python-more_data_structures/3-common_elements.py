#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    else:
        common_set = set(set_1) & set(set_2)
        return common_set

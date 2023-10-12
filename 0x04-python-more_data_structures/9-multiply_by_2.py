#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_list = list(a_dictionary)
    new_dict = {}
    for item in dict_list:
        new_dict[item] = a_dictionary[item] * 2
    return new_dict

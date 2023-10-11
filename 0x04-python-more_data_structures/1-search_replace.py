#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    new_list = []
    for item in my_list:
        if search == item:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

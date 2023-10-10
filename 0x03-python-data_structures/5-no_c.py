#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for s in my_string:
        if s == 'c' or s == 'C':
            continue
        new_str.append(s)
    final_string = "".join(new_str)
    return final_string

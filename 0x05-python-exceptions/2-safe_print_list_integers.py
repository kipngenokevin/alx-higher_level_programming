#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    j = 0
    while n < x:
        try:
            print("{:d}".format(my_list[n]), end="")
        except (ValueError, TypeError):
            j += 1
            pass
        n += 1
    print()
    return (n - j)

#!/usr/bin/python3
""" This module with class MyList that inherits from list"""


class MyList(list):
    """ def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)
        all the elements of the list will be of type int
        """
        sorted_list = sorted(self)
        print('[', end='')
        for i, item in enumerate(sorted_list):
            if i == len(sorted_list) - 1:
                end = ''
            else:
                end = ', '
            print(item, end=end)
        print(']')

#!/usr/python3
"""This module has a function that prints a square
with the character #
"""


def print_square(size):
    """This function prints square with #
    size is the size length of the square
    size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for num in range(size):
        for n in range(size):
            print("#", end="")
        print()

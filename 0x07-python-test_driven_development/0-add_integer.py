#!/usr/bin/python3
"""This module Returns an integer: the addition of a and b
a and b must be integers or floats, otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """add_integer returns addition of two ints.
    Typecast any float values into integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
""" module with function that
returns True of false depending on whether
an object is the instance of the class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly
    an instance of the specified class  otherwise, false
    """
    return type(obj) == a_class

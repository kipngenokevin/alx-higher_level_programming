#!/usr/bin/python3
"""This module demonstrates the use of isinstance"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the objec
    is an instance of a class that inherited from, the specified class
    otherwise False.
    """
    return isinstance(obj, a_class)
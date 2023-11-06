#!/usr/bin/python3
"""This module has a class with public methods"""


class BaseGeometry:
    """ Base class with a function to perform area"""

    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value
        you can assume name is always a string
        if value is not an integer: raise a TypeError
        if value is less or equal to 0: raise a ValueError
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

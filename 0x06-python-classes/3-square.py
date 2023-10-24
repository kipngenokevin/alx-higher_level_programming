#!/usr/bin/python3
""" This module Write a class Square
that defines a square by: (based on 1-square.py)
"""


class Square:
    """A class to represent a square
    Attributes:
        __size(int)
    """
    def __init__(self, size=0):
        """This code performs checks on size
        raise an exception if it is less than 0
        raise an exception if it is not an int
        """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This function returns the area
        Args:
            self
        """
        return self.__size * self.__size

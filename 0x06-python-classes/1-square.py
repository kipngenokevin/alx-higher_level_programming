#!/usr/bin/python3
"""This is the first module
It sets a private variable for the class Square
"""


class Square:
    """class Square.
    This class initiates the value of size of square
    Attributes:
        __size(int, optional)
    """
    def __init__(self, size=None):
        """This function sets defines private var size.
        Args:
            self
            size
        Return:
            None
        """
        self.__size = size

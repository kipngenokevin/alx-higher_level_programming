#!/usr/bin/python3
""" This module Write a class Square
that defines a square by: (based on 1-square.py)
"""


class Square:
    """A class to represent a square
    Attributes:
        __size(int)
    """
    def __init__(self, size=0, position=(0, 0)):
        """This code performs checks on size
        raise an exception if it is less than 0
        raise an exception if it is not an int
        """
        self.size = size
        self.position = position

    def area(self):
        """This function returns the area
        Args:
            self
        """
        return self.__size * self.__size

    @property
    def size(self):
        """This function returns the value of size.
        Args:
            self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This returns the value stored at position"""
        return self.__position

    @position.setter
    def position(self, value):
        """This sets the values of position.
        It goes through rigorous checks
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints out the square of size:
        It does so size no of times
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

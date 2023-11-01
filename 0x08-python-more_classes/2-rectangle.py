#!/usr/bin/python3
"""This module has a class Rectangle.
Rectangle takes two attributes.
Height and width, passed to the class during init.
"""


class Rectangle:
    """Class Rectangle sets a rectangle with
    height and width.
    Checks if both height and width are intgers
    And are greater than zero.
    """
    def __init__(self, width=0, height=0):
        """The init function passes the height and width of the
        rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This function returns the value stored in private var width"""
        return self.__width

    @property
    def height(self):
        """This function returns the value stored in height
        height is a private variable too"""
        return self.__height

    @width.setter
    def width(self, width):
        """This function sets the value of the width.
        It checks if it is an integer.
        If not an integer, it raises a TypeError.
        If not greater than zero, raise a ValueError.
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """This function sets the value of height.
        If height is not an integer, raise a TypeError.
        If height is less than zero, raise a ValueError.
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """This function returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This funtion returns the perimeter of a rectangle"""
        return 2 * (self.__width + self.__height)

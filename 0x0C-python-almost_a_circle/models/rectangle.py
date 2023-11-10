#!/usr/bin/python3
"""This module has class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ inherits from Base
    Private instance attributes,
    each with its own public getter and setter:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes
        each with its own public getter and setter
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return private instance width"""
        return self.__width

    @property
    def height(self):
        """Return private instance height"""
        return self.__height

    @property
    def x(self):
        """Return private instance x"""
        return self.__x

    @property
    def y(self):
        """Return private instance y"""
        return self.__y

    @width.setter
    def width(self, width):
        """Sets the value of width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """Sets the value of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """Sets the value of x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """Sets the value of y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

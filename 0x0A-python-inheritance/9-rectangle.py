#!/usr/bin/python3
"""This module has a class with public methods"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class that inherits from baseGeometry class"""

    def __init__(self, width, height):
        """ width and height must be private. No getter or setter
        width and height must be positive integers,
        validate by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """This is the user friendly output about the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """This function returns the area"""
        return self.__width * self.__height

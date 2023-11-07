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

#!/usr/bin/python3
"""This module contains classs Square
Square inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method returns the correct __str__"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This method returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

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

    def update(self, *args, **kwargs):
        """This module updates class Square attributes"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs and not args:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """This outputs the dictionary representation of square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

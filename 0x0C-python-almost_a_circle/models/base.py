#!/usr/bin/python3
""" This module contains the base class for this project.
class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """Class Base has the following
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """if id is not None, assign the public instance attribute id
        with this argument value
        you can assume id is an integer
        otherwise, increment __nb_objects
        assign the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

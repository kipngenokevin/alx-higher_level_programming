#!/usr/bin/python3
"""This module has a class with public methods"""


class BaseGeometry:
    """ Base class with a function to perform area"""

    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

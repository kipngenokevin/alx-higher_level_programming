#!/usr/bin/python3
"""This is a module with class student"""


class Student:
    """This class student holds the following data
    first_name
    last_name
    age
    all these attributes are public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes the public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method
        retrieves a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        serialized_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                serialized_data[attr] = getattr(self, attr)
        return serialized_data

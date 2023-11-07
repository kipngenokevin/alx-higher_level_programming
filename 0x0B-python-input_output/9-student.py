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

    def to_json(self):
        """ public method
        retrieves a dictionary representation of a Student
        """
        serialized_data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_data[key] = value
        return serialized_data

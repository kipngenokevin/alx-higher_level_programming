#!/usr/bin/python3
""" This module contains the base class for this project.
class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
to avoid duplicating the same code (by extension, same bugs)
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries:
        list_dictionaries is a list of dictionaries
        If list_dictionaries is None or empty
        return the string: "[]"
        return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if "size" in dictionary:
            dummy_instance = cls(1)
        else:
            dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                json_list = cls.from_json_string(content)
                instances_list = [cls.create(**item) for item in json_list]
                return instances_list
        except FileNotFoundError:
            return []

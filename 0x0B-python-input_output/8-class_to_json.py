#!/usr/bin/python3
""" This module has function def class_to_json(obj):"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object:
    """
    serialized_data = {}
    # loop through the objects attributes
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return serialized_data

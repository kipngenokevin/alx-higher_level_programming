#!/usr/bin/python3
""" This is a module that adds items to a list and saves them """
import sys
import json
from os.path import isfile
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_items_to_list_and_save(arguments, filename):
    """This function adds arguments to the filename """
    my_list = []
    if isfile(filename):
        my_list = load_from_json_file(filename)
    """ Add arguments to my_list """
    my_list.extend(arguments)
    """ Save to json file """
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    """ Check if the arguments are provided """
    arguments = sys.argv[1:]
    filename = "add_item.json"
    add_items_to_list_and_save(arguments, filename)

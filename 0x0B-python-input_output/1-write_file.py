#!/usr/bin/python3
""" This module has a function that writes text into a file """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    returns the number of characters written:
    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_written = file.write(text)
        return char_written

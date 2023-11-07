#!/usr/bin/python3
""" This module contains function to append text to a file """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    returns the number of characters added:
    If the file doesn’t exist, it should be created
    """
    with open(filename, 'a+', encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written

#!/usr/bin/python3
"""This module has a a function that
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prototype: def text_indentation(text):
    text must be a string, otherwise raise a TypeError
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    in_new_line = True
    for t in text:
        if t == '.' or t == '?' or t == ':':
            in_new_line = True
            print(t)
            print()
        else:
            if in_new_line:
                in_new_line = False
                t = t.lstrip()
            print(t, end="")

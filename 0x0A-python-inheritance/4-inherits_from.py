#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object


"""


def inherits_from(obj, a_class):
    """
    Returns the list of available attributes and methods of an object
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

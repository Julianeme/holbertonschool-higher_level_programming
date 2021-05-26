#!/usr/bin/python3
"""
    Returns the result of a + b, works only with integers and floats

    b value has a preinitialized value
"""


def add_integer(a, b=98):
    """
        Returns the add of a and b, always casts floats into ints
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

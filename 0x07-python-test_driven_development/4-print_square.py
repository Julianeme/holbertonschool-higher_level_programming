#!/usr/bin/python3
"""
    Returns the concatenation of
    first name and last name
    only works with strings
"""


def print_square(size):
    """
        Returns the input matrix divided by div variable
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    x = 0
    line = "#" * size
    while x < size:
        print(line)
        x += 1

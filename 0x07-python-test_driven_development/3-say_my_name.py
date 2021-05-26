#!/usr/bin/python3
"""
    Returns the concatenation of
    first name and last name
    only works with strings
"""


def say_my_name(first_name, last_name=""):
    """
        Returns the input matrix divided by div variable
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

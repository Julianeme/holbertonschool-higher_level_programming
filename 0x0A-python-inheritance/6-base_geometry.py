#!/usr/bin/python3
"""
    Creating an class with an exception


"""


class BaseGeometry:
    """
    An empty class with a execption message
    """
    def area(self):
        raise Exception("area() is not implemented")

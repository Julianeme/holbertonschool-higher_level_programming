#!/usr/bin/python3
"""
    Base class for geometric figures


"""


class BaseGeometry:
    """
    Checks and verifications only for a base class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

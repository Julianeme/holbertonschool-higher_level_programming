#!/usr/bin/python3
"""
    Base class BaseGeometry and and subclass Rectangle


"""


class BaseGeometry:
    """
    Base class for geomtry which checks input values
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle (BaseGeometry):
    """
        using inheritance to check for valid input values

    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("heigh", height)

        self.__width = width
        self.__height = height

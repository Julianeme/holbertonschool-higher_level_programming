#!/usr/bin/python3
"""
    Returns the result dividing each value of matrix
    by the div value. works only with integers and floats
    div value should be diff than zero
"""

class BaseGeometry:
    """
        Returns the input matrix divided by div variable
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
        Returns the input matrix divided by div variable
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("heigh", height)

        self.__width = width
        self.__height = height






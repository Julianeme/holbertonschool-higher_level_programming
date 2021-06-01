#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object


"""

class BaseGeometry:
    '''Just defining an empty class to start building it step by step!!!!!'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle (BaseGeometry):
    '''Just defining an empty class to start building it step by step!!!!!'''

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("heigh", height)

        self.__width = width
        self.__height = height






#!/usr/bin/python3
"""
    Base class BaseGeometry and and subclass Rectangle


"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """
        using inheritance to check for valid input values

    """

    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

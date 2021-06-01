#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    Base class BaseGeometry and and subclass Rectangle


"""


class Rectangle (BaseGeometry):
    """
        using inheritance to check for valid input values

    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

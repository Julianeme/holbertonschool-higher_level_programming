#!/usr/bin/python3
"""
    Base class BaseGeometry and and subclass Rectangle


"""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """
        instances area and str magic funtions added

    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

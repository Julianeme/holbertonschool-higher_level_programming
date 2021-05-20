#!/usr/bin/python3
'''Gonna start building a class Rectangle step by step!!!!'''


class Rectangle:
    '''Just defining an empty class to start building it step by step!!!!!'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is int:
                self.__width = value
            elif type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is int:
                self.__height = value
            elif type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")

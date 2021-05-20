#!/usr/bin/python3
'''Gonna start building a class Rectangle step by step!!!!'''


class Rectangle:
    '''Just defining an empty class to start building it step by step!!!!!'''
    def __init__(self, width=0, height=0):
        '''contructor for width and height'''
        self.width = width
        self.height = height

        @property
        def width(self):
            '''getter'''
            return self.__width

        @width.setter
        def width(self, value):
            '''setter, checks for the right tipe of widht'''
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            '''getter for height, private'''
            return self.__height

        @height.setter
        def height(self, value):
            '''checks that height has a valid value'''
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

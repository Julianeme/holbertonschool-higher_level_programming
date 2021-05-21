#!/usr/bin/python3
'''Gonna start building a class Rectangle step by step!!!!'''


class Rectangle:
    '''Just defining an empty class to start building it step by step!!!!!'''
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        '''contructor for width and height'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        a = ""
        if self.__width != 0 and self.__height != 0:
            for high in range(self.__height):
                for wide in range(self.__width):
                    a = a + '#'
                a += '\n'
            a = a[:-1]
        return a

    def __repr__(self):
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        if Rectangle.number_of_instances < 0:
            Rectangle.number_of_instances = 0
        print("Bye rectangle...")

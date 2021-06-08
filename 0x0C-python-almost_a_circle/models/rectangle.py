#!/usr/bin/python3
"""
    Rectangle class will ihnerite from base superclass


"""
from models.base import Base


class Rectangle(Base):
    """
    id: is inherited from the Base superclass
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for widht parameter'''
        return self.__width

    @width.setter
    def width(self, wide):
        '''setter, checks for the right type of widht'''
        if type(wide) is not int:
            raise TypeError("width must be an integer")
        elif wide <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = wide

    @property
    def height(self):
        '''getter for height parameter'''
        return self.__height

    @height.setter
    def height(self, high):
        '''setter, checks for the right type of height'''
        if type(high) is not int:
            raise TypeError("height must be an integer")
        elif high <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = high

    @property
    def x(self):
        '''getter for x parameter'''
        return self.__x

    @x.setter
    def x(self, xs):
        '''setter, checks for the right type of x offset'''
        if type(xs) is not int:
            raise TypeError("x must be an integer")
        elif xs < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = xs

    @property
    def y(self):
        '''getter for y parameter'''
        return self.__y

    @y.setter
    def y(self, ys):
        '''setter, checks for the right type of y offset'''
        if type(ys) is not int:
            raise TypeError("y must be an integer")
        elif ys < 0:
            raise TypeError("y must be >= 0")
        else:
            self.__y = ys

    def area(self):
        '''returns the area of a rectangle'''
        return (self.height * self.width)

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        if self.height == 0 or self.width == 0:
            print()
        else:
            print("\n" * self.y, end="")
            for i in range(self.height):
                print(" " * self.x, end="")
                for j in range(self.width):
                    print("#", end="")
                print()

    def __str__(self):
        '''str magic method returns the characteristics of the rectangl'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''updates the attributes of the rectangle from terminal'''
        if len(args) > 0:
            for index, word in enumerate(args):
                if index == 0:
                    self.index = word
                if index == 1:
                    self.width = word
                if index == 2:
                    self.height = word
                if index == 3:
                    self.x = word
                if index == 4:
                    self.y = word
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

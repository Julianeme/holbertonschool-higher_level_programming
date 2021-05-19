#!/usr/bin/python3
'''gets the size of the square'''


class Square:
    '''gets the size in a private attribute'''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        elif type(value) is not int:
                    raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

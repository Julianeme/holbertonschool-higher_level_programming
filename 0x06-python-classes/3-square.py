#!/usr/bin/python3
'''gets the size of the square'''


class Square:
    '''gets the size in a private attribute'''

    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

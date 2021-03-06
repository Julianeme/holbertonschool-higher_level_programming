#!/usr/bin/python3
'''gets the size of the square'''


class Square:
    '''gets the size in a private attribute'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    def my_print(self):
        j = 0
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1])
            while j < self.position[1]:
                print("_", end="")
                j += 1
            print()
            for i in range(self.__size):
                j = 0
                while j < self.position[1]:
                    print("_", end="")
                    j += 1
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

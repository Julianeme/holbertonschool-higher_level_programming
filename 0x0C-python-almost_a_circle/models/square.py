#!/usr/bin/python3
"""
    Rectangle class will ihnerite from base superclass


"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    id: is inherited from the Base superclass
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        '''getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter, checks for the right tipe of size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        '''updates the parameters of a square from terminal'''
        if len(args) > 0:
            commands = ['id', 'size', 'x', 'y']
            i = 0
            for words in args:
                setattr(self, commands[i], words)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        "Returns the dictionary representation of a Rectangle"
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

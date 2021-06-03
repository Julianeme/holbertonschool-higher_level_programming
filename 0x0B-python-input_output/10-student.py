#!/usr/bin/python3
"""
    Base class BaseGeometry and and subclass Rectangle


"""


class Student:
    """
        instances area and str magic funtions added

    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        ref_dict = {}
        if isinstance(attrs, list):
            for attributes in attrs:
                if attributes in self.__dict__:
                    ref_dict[attributes] = self.__dict__[attributes]
            return ref_dict
        return self.__dict__

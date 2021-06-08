#!/usr/bin/python3
"""
    Base class for the project


"""
import json
from models.rectangle import Rectangle



class Base:
    '''Base class for the project!!!!'''
    __nb_objects = 0

    def __init__(self, id=None):
        """
        id: if not provided the program will assign a sencuential one
        """

        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dic = []
        for element in list_objs:
            list_dic.append(cls.to_dictionary(element))
        with open(cls.__name__ + '.json', mode="w",
                  encoding="UTF8") as my_file:
            return(my_file.write(cls.to_json_string(list_dic)))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        a_inst = Rectangle(1, 1, 1, 1)
        a_inst.Rectangle.update(cls, **dictionary)

    @classmethod
    def load_from_file(cls):
        res = []
        if ((open(cls.__name__ + '.json') as my_file) is None):
            return res
        else
        with open(cls.__name__ + '.json', mode="w",
                  encoding="UTF8") as my_file:
            return(my_file.write(cls.to_json_string(list_dic)))

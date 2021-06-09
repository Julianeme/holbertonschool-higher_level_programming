#!/usr/bin/python3
"""
    Base class for the project


"""
import json


class Base:
    '''Base class for the project!!!!'''
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initial definition of the variables
        """

        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        list_dic = []
        if list_objs is not None:
            for element in list_objs:
                list_dic.append(cls.to_dictionary(element))
        else:
            list_dic = []
        with open(cls.__name__ + '.json', mode="w",
                  encoding="UTF8") as my_file:
            return(my_file.write(cls.to_json_string(list_dic)))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == 'Rectangle':
            a_inst = cls(1, 1)
        else:
            a_inst = cls(1)
        a_inst.update(**dictionary)
        return a_inst

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + '.json'
        list_f = []
        try:
            l_list = []
            with open(file_name, 'r', encoding="UTF8") as f:
                l_list = cls.from_json_string(f.read())
                for i in range(len(l_list)):
                    list_f.append(cls.create(**l_list[i]))
        except:
            list_f = []
        return list_f

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes and in CSV'''
        list_dic = []
        if list_objs is not None:
            for element in list_objs:
                list_dic.append(cls.to_dictionary(element))
        else:
            list_dic = []
        with open(cls.__name__ + '.cvs', mode="w",
                  encoding="UTF8") as my_file:
            return(my_file.write(cls.to_json_string(list_dic)))

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes from CSV'''
        file_name = cls.__name__ + '.cvs'
        list_f = []
        try:
            l_list = []
            with open(file_name, 'r', encoding="UTF8") as f:
                l_list = cls.from_json_string(f.read())
                for i in range(len(l_list)):
                    list_f.append(cls.create(**l_list[i]))
        except:
            list_f = []
        return list_f

#!/usr/bin/python3
"""
    function that writes an Object to a text file,
    using a JSON representation

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Checks and verifications only for a base class

    """
    with open(filename, mode="w", encoding="UTF8") as my_file:
        return(my_file.write(json.dumps(my_obj)))

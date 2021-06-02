#!/usr/bin/python3
"""
    function that creates an Object from a “JSON file”:

"""
import json


def load_from_json_file(filename):
    """
    Checks and verifications only for a base class

    """
    with open(filename, mode="r", encoding="UTF8") as my_file:
        return(json.load(my_file))

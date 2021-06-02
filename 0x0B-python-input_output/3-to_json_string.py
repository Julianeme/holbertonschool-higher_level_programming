#!/usr/bin/python3
"""
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added

"""
import json


def to_json_string(my_obj):
    """
    Checks and verifications only for a base class

    """
    return json.dumps(my_obj)

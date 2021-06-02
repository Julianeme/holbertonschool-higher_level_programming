#!/usr/bin/python3
"""
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added

"""


def append_write(filename="", text=""):
    """
    Checks and verifications only for a base class

    """
    with open(filename, mode="a", encoding="UTF8") as my_file:
        return(my_file.write(text))

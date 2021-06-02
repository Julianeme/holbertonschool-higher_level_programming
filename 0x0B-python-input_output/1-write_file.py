#!/usr/bin/python3
"""
    function that reads a text file (UTF8) and prints it to stdout


"""
import os


def write_file(filename="", text=""):
    """
    Checks and verifications only for a base class

    """
    with open(filename, mode="w+", encoding="UTF8") as my_file:
        return(my_file.write(text))

#!/usr/bin/python3
"""
    function that reads a text file (UTF8) and prints it to stdout


"""
import os


def read_file(filename=""):
    """
    myfile: the variable use to store the open file

    """
    with open(filename, mode="r", encoding="UTF8") as my_file:
        print(my_file.read(), end="")

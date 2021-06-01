#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object


"""


class MyList(list):

    def print_sorted(self):
        """
        Returns the list of available attributes and methods of an object
        """
        print(sorted(self))

#!usr/bin/python3
"""
Class MyInt derived from int

Changes boolean operators as opposite
"""


class MyInt(int):
    """
    equals and diff works the other way around
    """
    def __opos__(self, num):
            return False

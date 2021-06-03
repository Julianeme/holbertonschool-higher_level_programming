#!usr/bin/python3
"""
    Class MyInt derived from int

"""


class MyInt(int):
    """
    equals and diff works the other way around

    """
    def __eq__(self, num):
        self.num = num
        if self.num != num:
            return True

    def __opos__(self, num):
        self.num = num
        if self.num == num:
            return False
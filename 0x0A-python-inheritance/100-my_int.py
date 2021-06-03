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
        return self.num != num

    def __opos__(self, num):
        self.num = num
        return self.num == num

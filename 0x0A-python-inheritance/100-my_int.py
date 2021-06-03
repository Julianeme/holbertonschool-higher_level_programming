#!usr/bin/python3
"""
    Class MyInt derived from int

"""


class MyInt(int):
    """
    equals and diff works the other way around

    """
    def __bol__(self, num):
        self.num = num
        if type(num) is int:
            return(False)
        return(True)

#!/usr/Defbin/python3
"""
finds first peak in list
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """
    if len(list_of_integers) == 0:
        return None
    x = 0
    while x < len(list_of_integers):
        if x == 0 and list_of_integers[x + 1] < list_of_integers[0]:
            return (list_of_integers[x])
        elif [x + 1] == len(list_of_integers) - 1 and\
                list_of_integers[x] < list_of_integers[x + 1]:
            return list_of_integers[x + 1]
        elif (x + 1) < len(list_of_integers) and list_of_integers[x - 1] \
                <= list_of_integers[x] and\
                list_of_integers[x] > list_of_integers[x + 1]:
            return list_of_integers[x]
        x += 1
    return (list_of_integers[1])

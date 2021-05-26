#!/usr/bin/python3
"""
    Returns the concatenation of
    first name and last name
    only works with strings
"""


def text_indentation(text):
    """
        Returns the input matrix divided by div variable
    """
    aux = ""
    pos = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while pos in range(len(text)):
        aux = aux + text[pos]
        if text[pos] == '.' or text[pos] == '?' or text[pos] == ':':
            aux = aux + '\n\n'
            if pos < (len(text) - 1) and text[(pos + 1)] == " ":
                pos += 1
        pos += 1
    print(aux)

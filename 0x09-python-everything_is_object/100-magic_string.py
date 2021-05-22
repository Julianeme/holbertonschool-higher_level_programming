#!/usr/bin/python3
def magic_string():
    magic_string.counter += 1
    return ("Holberton " + (", Holberton" * (magic_string.counter - 1)))
magic_string.counter = 0
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_d = a_dictionary.copy()
    for value in copy_d:
        copy_d[value] *= 2
    return(copy_d)

#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if not my_list:
        return(None)
    for x in my_list:
        if x > a:
            a = x
    return(a)

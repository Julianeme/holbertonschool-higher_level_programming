#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for i in range(len(sorted_dict)):
        print("{}: {}".format(sorted_dict[i], a_dictionary[sorted_dict[i]]))

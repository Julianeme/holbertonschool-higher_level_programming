#!/usr/bin/python3
"""
    a script that adds all arguments to a
    Python list, and then save them to a file

"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    a = load_from_json_file("add_item.json")
except:
    a = []
for element in sys.argv[1:]:
    a.append(element)
save_to_json_file(a, "add_item.json")

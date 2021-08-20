#!/usr/bin/python3
"""
   script that takes in a letter and sends a POST
   request to http://0.0.0.0:5000/search_user with the letter
   as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":

    data = {'key': 'value'}
    q = ""
    if len(argv) > 1:
        q = "/"+ argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user" + q, data)
    if type(req.text) == dict and req.text is not None:
        print("[{}] {}: {}".format(req.text[id], req.text[name]))
    elif type(req.text) == dict or len(argv) == 1:
        print("No result")
    else:
        print("Not a valid JSON")

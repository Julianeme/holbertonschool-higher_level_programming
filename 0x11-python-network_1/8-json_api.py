#!/usr/bin/python3
"""
   script that takes in a letter and sends a POST
   request to http://0.0.0.0:5000/search_user with the letter
   as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":

    data_d = {'q': ""}
    if len(argv) > 1:
        data_d['q'] = argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data=data_d)
    try:
        json_req = req.json()
        if len(json_req) > 0:
            print("[{}] {}".format(json_req['id'], json_req['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).
"""

import urllib.request
from sys import argv
from urllib import error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as error_code:
        print("Error code: {}".format(error_code.__dict__.get('code')))

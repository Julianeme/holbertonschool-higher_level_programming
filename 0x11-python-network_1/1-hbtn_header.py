#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
from sys import argv

if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status/") \
            as response:
        print("{}".format(response.getheader('X-Request-Id')))

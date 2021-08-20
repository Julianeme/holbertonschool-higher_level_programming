#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv
import urllib

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        html = response.read()
        html = html.decode('utf-8')
    print(html)

#!/usr/bin/python3
"""
  script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":

    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))

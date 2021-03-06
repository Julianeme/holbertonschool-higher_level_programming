#!/usr/bin/python3
"""
   script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
"""
import requests.auth
import requests
from sys import argv

if __name__ == "__main__":
    try:
        id = requests.get(
            'https://api.github.com/user', auth=(argv[1], argv[2]))
        id_json = id.json()
        print(id_json['id'])
    except:
        print("None")

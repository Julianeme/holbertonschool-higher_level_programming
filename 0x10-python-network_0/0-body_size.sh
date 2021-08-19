#!/bin/bash
# script that takes in a URL, sends a request to it,and displays its size

curl -s Content-Length: "http://$1"

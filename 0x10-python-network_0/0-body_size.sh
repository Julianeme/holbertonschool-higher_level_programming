#!/bin/bash
# script that takes in a URL, sends a request to it,and displays its size

curl -sI "$1" | grep -i content-length | awk '{print $2}'

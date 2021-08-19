#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sH "X-HolbertonSchool-User-Id: 98" -GET "$1"

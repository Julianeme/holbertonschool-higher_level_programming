#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sH "email: hr@holbertonschool.com&subject: I will always be here for PLD" -POST "$1"

#!/bin/bash
# Bash script that takes in a URL and displays
# all HTTP methods the server will accept

for method in OPTIONS GET HEAD POST PUT DELETE TRACE CONNECT ; do 
    echo -e "\n\nTrying $method\n\n" 
    echo -e "$method / HTTP/1.1\nHost: server-hostname\nConnection: close\n\n" | nc server-hostname 80 | head 
    sleep 2
done

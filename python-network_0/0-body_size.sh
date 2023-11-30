#!/bin/bash
# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a request and get the size of the response body
size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

# Check if the Content-Length header is present in the response
if [ -z "$size" ]; then
    echo "Unable to determine the size of the response body."
else
    echo "Size of the response body: ${size} bytes"
fi


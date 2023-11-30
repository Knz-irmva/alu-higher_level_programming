#!/bin/bash
# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a GET request and display the body if the status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    body=$(curl -s "$url")
    echo "Response Body:"
    echo "$body"
else
    echo "Request failed with status code: $response"
fi


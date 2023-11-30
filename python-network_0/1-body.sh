#!/bin/bash
# Check if a URL is provided as an argument
[ $# -eq 0 ] && { echo "Usage: $0 <URL>"; exit 1; }

# Use curl to send a GET request and display the body for a 200 status code response
curl -s -w "%{http_code}" "$1" | awk 'NR>1 {print} END {exit !/^200/}'


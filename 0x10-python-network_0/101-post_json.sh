#!/usr/bin/bash
#displays the body of the response, including the contents of a JSON file
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"

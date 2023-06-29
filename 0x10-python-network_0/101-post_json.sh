#!/usr/bin/bash
#displays the body of the response, including the contents of a JSON file
curl -sX POST -d @"$2" "$1" -H "Content-Type: application/json"

#!/bin/bash
#takes a URL as input and displays all the HTTP methods accepted by the server
curl -sI "$1" | grep -i "Allow:"

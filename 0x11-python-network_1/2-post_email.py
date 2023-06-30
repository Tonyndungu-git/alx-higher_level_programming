#!/usr/bin/python3
""" sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8) """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    req = urllib.request.Request(sys.argv[1], data=data, method='POST')

    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.read().decode('utf-8')
        print(body)

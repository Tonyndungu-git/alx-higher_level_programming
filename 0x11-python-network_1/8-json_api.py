#!/usr/bin/python3

""" takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""

import requests
import sys

if __name__ == "__main__":

    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    response = requests.post(url, data=data)
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

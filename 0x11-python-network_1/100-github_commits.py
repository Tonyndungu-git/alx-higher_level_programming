#!/usr/bin/python3

""" Python script that takes 2 arguments in order to
solve the challenge stated """
import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")

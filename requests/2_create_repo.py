"""
This script creates a new repository on GitHub using the GitHub API.
"""
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth


def create_repo(url: str) -> dict:
    """
    Create a new repository on GitHub using the GitHub API.

    Parameters:
    - url (str): The URL to create the repository.

    Returns:
    - dict: A dictionary with the JSON response from the GitHub API after creating the repository.
    """
    r = requests.post(url,
                      timeout=5,
                      auth=HTTPBasicAuth('trainingprofile', "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"),
                      json={
                          "name": 'repo-created-with-api',
                          "private": True,
                          "has_wiki": False,
                          'Accept': 'application/vnd.github+json'
                      },
                      )

    print(f"Response status code: {r.status_code}")

    return r.json()


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)

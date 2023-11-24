"""
This script makes a GET request to the GitHub API with authentication
and prints the response status code, the total number of repositories,
and the response headers.
"""

import requests
from requests.auth import HTTPBasicAuth


def get_with_auth(url: str) -> (int, dict):
    """
    Make a GET request to the specified URL with authentication.

    Parameters:
    - url (str): The URL to make the GET request to.

    Returns:
    - int: The length of the JSON response.
    - dict: The response headers.
    """
    r = requests.get(url,
                     timeout=5,
                     auth=HTTPBasicAuth('vr8686', "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"))

    print(f"Response status code: {r.status_code}")

    return len(r.json()), r.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")

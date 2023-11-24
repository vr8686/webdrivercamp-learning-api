"""
This script retrieves repository information from the GitHub API.
"""

import requests


def get_repos(url):
    """
    Retrieve repository information from the given GitHub API URL.

    Parameters:
    - url (str): The GitHub API URL to fetch repository information.

    Returns:
    - list: A list of repository items sorted by owner's login.
    """
    r = requests.get(url, timeout=5)
    print(f"Response status code: {r.status_code}")

    # Deserializing data from HTTP request
    json_response = r.json()

    total_count = json_response['total_count']
    print(f"Total count of found items: {total_count}")

    # Returning items sorted by owner login in alphabetical order
    return sorted(json_response['items'], key=lambda x: x['owner']['login'])


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)

"""
This script updates the description of a GitHub repository using the GitHub API.

Note:
    - The script uses a PATCH request to update the repository's description.
    - The updated description is set to 'I know Python Requests!'.
    - Raises AssertionError: If the assertion to check the updated repository's description fails.
"""
import requests
from requests.auth import HTTPBasicAuth


def update_repo(url: str) -> dict:
    """
    Update the description of a GitHub repository using the GitHub API.

    Parameters:
    - url (str): The GitHub API URL for the specific repository.

    Returns:
    - dict: A dictionary with the JSON response from the GitHub API after updating the repository.
    """
    r = requests.patch(url,
                       timeout=5,
                       auth=HTTPBasicAuth('vr8686', "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"),
                       json={
                           "description": 'I know Python Requests!',
                           'Accept': 'application/vnd.github+json'
                       },
                       )

    print(f"Response status code: {r.status_code}")
    # Returning JSON decoded response
    return r.json()


if __name__ == '__main__':
    owner = "vr8686"
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'

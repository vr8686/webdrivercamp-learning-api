"""
This script deletes a GitHub repository using the GitHub API.
"""
import requests
from requests.auth import HTTPBasicAuth


def delete_repo(url):
    """
    Delete a GitHub repository using the GitHub API.

    Parameters:
    - url (str): The GitHub API URL for the specific repository to be deleted.

    Note:
    - The function uses a DELETE request to delete the specified repository.
    """
    r = requests.delete(url,
                        timeout=5,
                        auth=HTTPBasicAuth('vr8686', "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"),
                        json={
                            "repo": 'repo-created-with-api',
                            "owner": 'vr8686',
                            'Accept': 'application/vnd.github+json'
                        },
                        )

    print(f"Response status code: {r.status_code}")


if __name__ == "__main__":
    owner = "vr8686"
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)

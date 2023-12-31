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
                        auth=HTTPBasicAuth('trainingprofile', "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"),
                        json={
                            "repo": 'repo-created-with-api',
                            "owner": 'trainingprofile',
                            'Accept': 'application/vnd.github+json'
                        },
                        )

    print(f"Response status code: {r.status_code}")


if __name__ == "__main__":
    owner = "trainingprofile"
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)

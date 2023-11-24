"""
This script retrieves details of a created repository from the GitHub API.

Note:
    - The script makes assertions to check specific properties of the repository.
    - If assertions fail, an AssertionError is raised, indicating the property that didn't match.
"""
import requests
from requests.auth import HTTPBasicAuth


def get_created_repo(url: str):
    """
    Retrieve details of a created repository from the given GitHub API URL.

    Parameters:
    - url (str): The GitHub API URL for the specific repository.

    Raises:
    - AssertionError: If any of the assertions fail.
    """
    r = requests.get(url,
                     timeout=5,
                     auth=HTTPBasicAuth('vr8686', "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"),
                     json={'Accept': 'application/vnd.github+json'}
                     )
    print(f"Response status code: {r.status_code}")

    repo = r.json()

    # Asserting the repo was created with proper parameters
    try:
        assert repo['has_wiki'] is False
        assert repo['private'] is True
        assert repo['name'] == 'repo-created-with-api'
        assert repo['owner']['login'] == 'vr8686'
    except AssertionError as e:
        print(f'Assertion Error - {e}')


if __name__ == "__main__":
    owner = "vr8686"
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    get_created_repo(url)

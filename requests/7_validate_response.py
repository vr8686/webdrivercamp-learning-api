"""
Module: 7_validate_response.py

This module defines a function to compare data from an API with data from a JSON file
and identify mismatches based on the planet name.
"""
import json
from pprint import pprint

import requests


def find_mismatched_data(url: str, file_name: str) -> dict:
    """
    Compare data from the API with data from the JSON file and find mismatches.

    Parameters:
    - url (str): The URL of the REST API.
    - file_name (str): The name of the JSON file.

    Returns:
    - dict: A dictionary containing mismatches organized by planet name.
    """

    # Get data from the API
    r = requests.get(url, timeout=10)
    results_api = r.json()['results']

    # Load data from the JSON file
    with open(file_name, "r", encoding="utf-8") as f:
        results_file = json.load(f)['results']

    # Check if the lengths of both data sources match
    if len(results_api) != len(results_file):
        raise ValueError("Mismatched data lengths")

    # Check if the keys of both data sources match
    keys_results_api = {tuple(sorted(d.keys())) for d in results_api}
    keys_results_file = {tuple(sorted(d.keys())) for d in results_file}
    if keys_results_api != keys_results_file:
        raise ValueError("Mismatched keys in data")

    # Create a dictionary to store mismatches
    mismatches = {}

    # Sort dictionaries by the planet name
    results_api_sorted = sorted(results_api, key=lambda x: x['name'])
    results_file_sorted = sorted(results_file, key=lambda x: x['name'])

    # Iterate over the sorted data and identify mismatches
    for i, dict_ in enumerate(results_api_sorted):
        for key in dict_:
            if dict_[key] != results_file_sorted[i][key]:
                if dict_['name'] not in mismatches:
                    mismatches[dict_['name']] = []
                mismatches[dict_['name']].append({key: {'Expected': results_file_sorted[i][key],
                                                        'Actual': dict_[key]}})

    return mismatches


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))

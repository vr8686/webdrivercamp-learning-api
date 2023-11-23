"""
This module provides a function to serialize a Python object to JSON format
and write it to a file.
"""

import json


def to_json_file(file_name: str):
    """
    Serialize a Python object to JSON format and write it to a file.

    Parameters:
    - file_name (str): The name of the file to write the JSON data to.

    Returns:
    - None
    """
    data_object = {"list": [1, 2, 3, 4, 5],
                   "tuple": (1, 2, 3, 4, 5),
                   "string": "Hello World!",
                   "bool": False,
                   "null": None,
                   "int": 123,
                   "float": 3.14,
                   "dict": {"abc": True, "Hello": "World", 10: [2, 3, 4]}}

    with open(file_name, "w", encoding='utf-8') as file:
        json.dump(data_object, file)


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"

    to_json_file(file_name)

    with open(file_name, "r", encoding='utf-8') as f:
        print(f.read())

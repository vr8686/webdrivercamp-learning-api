"""
Module docstring: This module contains a function for reading the line 3 in the file.
"""


def read_a_file(filename: str):
    """
    Read data from the specified file.

    Parameters:
    - filename (str): The name of the file to read from.

    Returns:
    - prints the 3rd line of file's content.
    """
    with open(filename, "r", encoding="utf-8") as reader:
        print(reader.readlines()[2])


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    read_a_file(file_name)

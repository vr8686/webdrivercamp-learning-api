"""
Module docstring: This module contains a function for appending data to a file.
"""


def append_to_file(data: str, file_name: str) -> int:
    """
    Append the provided data to the specified file.

    Parameters:
    - data (str): The data to be appended to the file.
    - filename (str): The name of the file to append the data to.

    Returns:
    - int: The number of characters added to the file.
    """
    with open(file_name, "a", encoding='utf-8') as ap_writer:
        ap_writer.write(data)
        return len(data)


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = "\nDon't Panic"

    print(f"Number of chars added: {append_to_file(data, file_name)}")

    data = "\nDon't Panic!!!"

    print(f"Number of chars added: {append_to_file(data, file_name)}")

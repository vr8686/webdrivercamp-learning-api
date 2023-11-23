"""
Module docstring: This module contains a function for writing data to a file.
"""


def write_to_file(data: str, filename: str) -> int:
    """
    Write the provided data to the specified file.

    Parameters:
    - data (str): The data to be written to the file.
    - filename (str): The name of the file to write the data to.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as writer:
        writer.write(data)
        return len(data)


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = """
    In the beginning the Universe was created. 
    This has made a lot of people very angry and been widely regarded as a bad move."""

    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    data = "Don't Panic"
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")

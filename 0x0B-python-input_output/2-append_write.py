#!/usr/bin/python3
"""Explains a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): File name to append to.
        text (str): The string to append to the file.
    Returns:
        The character count count appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)


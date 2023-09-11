#!/usr/bin/python3

"""Accounts for a class-checking function."""


def is_same_class(obj, a_class):
    """Looks if an object is an instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        If obj is exact instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

#!/usr/bin/python3

"""Delineate an object feature lookup function."""


def lookup(obj):
    """Return object's list available attributes."""
    return (dir(obj))


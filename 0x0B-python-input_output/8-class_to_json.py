#!/usr/bin/python3
"""Explains a Python class-to-JSON function."""


def class_to_json(obj):
    """Return  a simple data structure dictionary representation."""
    return obj.__dict__

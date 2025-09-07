#!/usr/bin/python3
"""This module defines a function that lists all attributes of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of obj."""
    return dir(obj)


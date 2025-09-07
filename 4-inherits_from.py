#!/usr/bin/python3
"""Function to check if object is subclass of a class (not exact match)"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class


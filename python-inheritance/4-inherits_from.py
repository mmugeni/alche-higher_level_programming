#!/usr/bin/python3
"""This module defines a function to check if an object inherits from
a specified class (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not exactly a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


#!/usr/bin/python3
"""Function to check if object is exactly instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly instance of a_class"""
    return type(obj) is a_class


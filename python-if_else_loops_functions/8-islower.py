#!/usr/bin/python3
def islower(c):
    """Return True if c is a lowercase letter, otherwise False."""
    if isinstance(c, str) and len(c) == 1:
        return ord('a') <= ord(c) <= ord('z')
    return False

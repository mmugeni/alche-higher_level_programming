#!/usr/bin/env python3
def no_c(my_string):
    """Return a new string with all 'c' and 'C' removed."""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a copy of the list with element replaced at idx, without modifying the original."""
    new_list = my_list[:]  # Make a shallow copy
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list

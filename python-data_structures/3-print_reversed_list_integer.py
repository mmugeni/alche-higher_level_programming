#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers in a list in reverse order, one per line."""
    for i in my_list[::-1]:
        print("{:d}".format(i))

#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

#!/usr/bin/python3
"""This module defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with size as private attribute."""

    def __init__(self, size):
        """Initialize a square with size."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)


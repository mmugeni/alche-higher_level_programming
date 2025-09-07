#!/usr/bin/python3
"""This module defines a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with private width and height validated by BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


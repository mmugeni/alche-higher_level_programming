#!/usr/bin/python3
"""This module defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an exception as area is not implemented."""
        raise Exception("area() is not implemented")


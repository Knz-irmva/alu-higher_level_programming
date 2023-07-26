#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a sqaure."""

    def _init_(self, size=0):
        """Initialize a new Sqaure.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size 

    def area(self):
        """Return the current area of the square."""
        return (self._size * self._size)


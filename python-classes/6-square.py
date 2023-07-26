#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (optional, default is 0).
            position (tuple): The position of the square (optional, default is (0, 0)).

        Raises:
            TypeError: If size is not an integer, or position is not a tuple of two positive integers.
            ValueError: If size is less than 0, or any value in position is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position to set.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
            ValueError: If any value in position is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(coord, int) for coord in value) or any(coord < 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # in stdout.

        If size is 0, print an empty line.
        position should be used by using space - Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


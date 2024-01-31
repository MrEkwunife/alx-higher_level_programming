#!/usr/bin/python3

"""this contain `print_square` function that prints a square"""

def print_square(size):
    """prints square of size `size`.
    Args:
        size (int)
    """

    if not isinstance(size, int):
            raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):        
        for _ in range(size):
            print("#", end="")
        print()

#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """this class inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

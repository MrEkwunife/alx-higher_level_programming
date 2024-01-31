#!/usr/bin/python3
"""tests for max _int functon"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_max_integer(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_scattered(self):
        """Test an un-ordered list of integers."""
        self.assertEqual(max_integer([4, 2, 1, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_empty(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_same(self):
        """Test list of same integers."""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()

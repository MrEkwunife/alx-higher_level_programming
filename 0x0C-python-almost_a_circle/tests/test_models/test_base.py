#!/usr/bin/python3
# File: test_base.py
# Author: Chimobi E.
"""
This is the test Module for the Base Class(unittest)

Unittest Classes:
    TestBase_instantiation - line 14
"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Unittest for testing the instantiation of the Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_increament(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(20)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, 20)
        self.assertEqual(b4.id, b1.id + 2)


if __name__ == '__main__':
    unittest.main()

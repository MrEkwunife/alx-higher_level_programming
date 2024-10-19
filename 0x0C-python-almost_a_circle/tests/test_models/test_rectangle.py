#!/usr/bin/python3
# File: test_rectangle.py
# Author: Chimobi E.
"""This modules uses unittest to the rectangle module
of the models package"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangleInstantiation(unittest.TestCase):
    """Inheriting from unittest.TestCase tests objects are correctly
    instantiated
    """

    def test_with_height_width(self):
        """Tests the instantiation of an object from the class"""
        rec1 = Rectangle(2, 5)
        self.assertIsInstance(rec1, Rectangle)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Tests the instantiation of an object from the class"""
        rec1 = Rectangle(2, 5)
        self.assertIsInstance(rec1, Rectangle)

    def test_with_height_width(self):
        """Tests the instantiation of an object from the class"""
        rec1 = Rectangle(2, 5)

        self.assertIsInstance(rec1, Rectangle)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 5)

    def test_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

        with self.assertRaises(TypeError):
            Rectangle([1, 2, 4, 6], 12, 2, 4)

        with self.assertRaises(TypeError):
            Rectangle(None, Rectangle(2, 4).id)

        with self.assertRaises(ValueError):
            Rectangle(0, 4, 2, 2)

        rec1 = Rectangle(7, 10)
        with self.assertRaises(ValueError):
            rec1.width = 0

    def test_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, {'age': 22, 'name': 'Chimobi'})

        with self.assertRaises(TypeError):
            Rectangle(Rectangle(9, 9).id, None)

        with self.assertRaises(ValueError):
            Rectangle(10, -6)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_with_id(self):
        rec1 = Rectangle(4, 8, id=9)
        rec2 = Rectangle(6, 12, id=12)
        rec3 = Rectangle(2, 3, id=7)

        self.assertEqual(rec1.id, 9)
        self.assertEqual(rec2.id, 12)
        self.assertEqual(rec3.id, 7)

    def test_with_no_id(self):
        rec1 = Rectangle(9, 12)
        rec2 = Rectangle(12, 9)

        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, rec1.id + 1)

    def test_x(self):
        rec1 = Rectangle(9, 12, 2)
        rec2 = Rectangle(12, 9, x=5)

        self.assertEqual(rec1.x, 2)
        self.assertEqual(rec2.x, 5)
        self.assertEqual(rec1.y, 0)

        with self.assertRaises(TypeError):
            Rectangle(8, 3, (1, 4, 5))

        with self.assertRaises(TypeError):
            Rectangle(2, 4, None)

        with self.assertRaises(ValueError):
            Rectangle(2, 4, -1)

        # But x can be zero (0)
        rec3 = Rectangle(2, 4, 0, id=12)
        self.assertEqual(rec3.id, 12)

    def test_with_y(self):
        rec1 = Rectangle(14, 24, y=9)

        self.assertEqual(rec1.y, 9)
        self.assertEqual(rec1.x, 0)

        with self.assertRaises(TypeError):
            Rectangle(12, 24, y=[2, 3, 6])

        with self.assertRaises(ValueError):
            Rectangle(9, 9, y=-1)

        # Can be reassigned to same type and correct value but not otherwise
        rec2 = Rectangle(9, 8, x=0, y=0)

        rec2.y = 6
        self.assertEqual(rec2.y, 6)

        with self.assertRaises(ValueError):
            rec2.y = -1
        with self.assertRaises(TypeError):
            rec2.y = (0, 0)

    def test_with_xy(self):
        rec1 = Rectangle(14, 14, 2, 4)
        rec2 = Rectangle(6, 12, y=2, x=4)
        rec3 = Rectangle(5, 10, x=5, y=5)

        self.assertEqual(rec1.x, 2)
        self.assertEqual(rec2.y, 2)
        self.assertEqual(rec2.x, 4)
        self.assertEqual(rec3.y, 5)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the rectangle class"""

    def test_area_small(self):
        r = Rectangle(2, 12, 0, 0, 0)
        self.assertEqual(24, r.area())

    def test_area_big(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(8, 2)
        r.width = 4
        r.height = 2
        self.assertEqual(8, r.area())

    def area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

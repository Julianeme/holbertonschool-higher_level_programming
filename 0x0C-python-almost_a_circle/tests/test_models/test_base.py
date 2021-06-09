#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Test class"""
    def test_id(self):
        """test empty and given id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 2)



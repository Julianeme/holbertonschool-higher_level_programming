#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_TestMaxInteger(self):
        self.assertEqual(max_integer([2, 5, 7, 1], 7)
        self.assertEqual(max_integer([0, 1, -8, 3], 3)
        self.assertEqual(max_integer([-2], -2)
    def test_empty_function(self):
        self.assertNone(max_integer([])

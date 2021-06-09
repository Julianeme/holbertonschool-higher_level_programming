#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import base
import rectangle


class TestMaxInteger(unittest.TestCase):
    def test_TestMaxInteger(self):
        self.assertEqual(max_integer([2, 5, 7, 1]), 7)
        self.assertEqual(max_integer([0, 1, -8, 3]), 3)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([-5, -8, - 15, -1, 0]), 0)
        self.assertEqual(max_integer([8]), 8)
        self.assertEqual(max_integer([1.3, 6.8, 4.4]), 6.8)
        self.assertEqual(max_integer([13.5, 6.8, 4.4]), 13.5)

    def test_empty_function(self):
        self.assertIsNone(max_integer([]))

    def test_string_error(self):
        self.assertRaises(TypeError, max_integer(["a"]))

    def test_char_error(self):
        self.assertRaises(TypeError, max_integer(["c", "d", "a", "z"]))

    def test_mix_num_error(self):
        self.assertRaises(TypeError, max_integer([2, 6, 6.3]))

if __name__=='__main__': unittest.main()

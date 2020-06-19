"""
Program: test_basic_list.py
Author: Daniel Meeker
Date: 6/19/2020

This program defines two functions, make_list and get_input
for the purpose of creating a list of user input. This file
tests the function make_list.
"""
import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic_list
import fun_with_collections.basic_list_exception as basic_list_exception


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [5, 5, 5])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-1')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()

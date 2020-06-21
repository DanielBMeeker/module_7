"""
Program: test_sort_and_search_array.py
Author: Daniel Meeker
Date: 6/21/2020

This program defines two functions to search or sort an array.
This file tests the functions as well as checking to make sure
that an error is raised if the user passes a list instead of
an array.
"""
import unittest
import array as arr
from fun_with_collections import sort_and_search_array as ssa
array_searched = arr.array('i', [0, 1, 2, 3, 4, 5])
value_searched = 2
invalid_value_searched = 6
array_to_sort = arr.array('i', [5, 3, 2, 4, 0, 1])
array_type_error = [0, 1, 2, 3, 4, 'five']


class MyTestCase(unittest.TestCase):
    def test_search_in_list(self):
        self.assertEqual(ssa.search_array(array_searched, value_searched), 2)

    def test_search_not_in_list(self):
        self.assertEqual(ssa.search_array(array_searched, invalid_value_searched), -1)

    def test_sort_list(self):
        self.assertEqual(ssa.sort_array(array_to_sort), array_searched)

    def test_conversion_error(self):  # test to verify an error is thrown if there are mismatching types in the array.
        self.assertRaises(TypeError, ssa.sort_array(array_type_error))


if __name__ == '__main__':
    unittest.main()

"""
Program: test_sort_and_search_list.py
Author: Daniel Meeker
Date: 6/19/2020

This program defines two functions, one for
searching lists and another for sorting
lists. This file tests the functions.
"""
import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as sort_and_search_list

list_searched = [0, 1, 2, 3, 4, 5]
value_searched = 2
invalid_value_searched = 6
list_to_sort = [5, 3, 2, 4, 0, 1]


class MyTestCase(unittest.TestCase):
    def test_search_in_list(self):
        self.assertEqual(sort_and_search_list.search_list(list_searched, value_searched), 2)

    def test_search_not_in_list(self):
        self.assertEqual(sort_and_search_list.search_list(list_searched, invalid_value_searched), -1)

    def test_sort_list(self):
        self.assertEqual(sort_and_search_list.sort_list(list_to_sort), list_searched)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as sort_and_search_list

list_searched = [0, 1, 2, 3, 4, 5]
value_searched = 2
invalid_value_searched = 6


class MyTestCase(unittest.TestCase):
    def test_search_in_list(self):
        self.assertEqual(sort_and_search_list.search_list(list_searched, value_searched), 3)

    def test_search_not_in_list(self):
        self.assertEqual(sort_and_search_list.search_list(list_searched, invalid_value_searched), -1)


if __name__ == '__main__':
    unittest.main()

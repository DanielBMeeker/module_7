import unittest
import array as arr
from fun_with_collections import sort_and_search_array as ssa
array_searched = arr.array('i', [0, 1, 2, 3, 4, 5])
value_searched = 2
invalid_value_searched = 6
array_to_sort = arr.array('i', [5, 3, 2, 4, 0, 1])


class MyTestCase(unittest.TestCase):
    def test_search_in_list(self):
        self.assertEqual(ssa.search_array(array_searched, value_searched), 2)

    def test_search_not_in_list(self):
        self.assertEqual(ssa.search_array(array_searched, invalid_value_searched), -1)

    def test_sort_list(self):
        self.assertEqual(ssa.sort_array(array_to_sort), array_searched)


if __name__ == '__main__':
    unittest.main()

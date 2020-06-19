"""
Program: sort_and_search_list.py
Author: Daniel Meeker
Date: 6/19/2020

This program defines two functions, one for
searching lists and another for sorting
lists.
"""


def sort_list(a_list):
    """
    This function takes in a list and sorts it.
    :param a_list: A list passed into the function to be sorted
    :return: returns the sorted list to where it is called
    """
    a_list.sort()
    return a_list
    # I tried to make it work without a return statement because sorting
    # the list should change the list in memory but the assertEqual function
    # in the testing required a list to be returned the way I wrote the test.
    # Rather than rewriting that test to try to figure out how to make it work
    # without a return I decided to add the return.


def search_list(a_list, value):
    """
    :param a_list: A list passed into the function to be searched
    :param value: The value being searched for in the list.
    :return: Index of object if in list. Returns -1 if not in list
    """
    if value not in a_list:
        return -1
    else:
        return a_list.index(value)

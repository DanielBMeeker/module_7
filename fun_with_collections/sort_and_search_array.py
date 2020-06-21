"""
Program: sort_and_search_array.py
Author: Daniel Meeker
Date: 6/21/2020

This program defines two functions to search or sort an array.
"""
import array as arr


def sort_array(a_array):
    """
    This function will take an array and sort it. It explicitly converts to an array
    in case the user tries to pass in a list. It has exception handling in case there
    is a type error.

    :param a_array: An array passed in to be sorted
    :return: returns the array after it has been sorted. Array's are mutable so returning it
             will change the array where it was called and you don't need to create a new array
             to hold the sorted original array.
    """
    try:
        a_array = arr.array('i', a_array)  # explicitly convert to array in case it comes in as a list
    except TypeError as e:
        return e
    a_list = a_array.tolist()  # now that it is explicitly an array convert back to list to use built in sort method
    a_list.sort()
    a_array = a_list
    return arr.array('i', a_array)  # convert sorted list back to array and return it


def search_array(a_array, value):
    """
    This function takes an array and a value and searches to see if the value is found in the array.

    :param a_array: The array to be searched
    :param value: The value being searched for in the array
    :return: Either the index of the first instance of the value being searched or -1 if value is not in array
    """
    try:
        a_array = arr.array('i', a_array)  # explicitly convert to array in case it comes in as a list
    except TypeError as e:
        return e
    if value not in a_array:
        return -1
    else:
        return a_array.index(value)
    pass

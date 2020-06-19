"""
Program: basic_list_exception.py
Author: Daniel Meeker
Date: 6/19/2020

This program defines two functions that work in conjunction
to create a list. The make_list function will now raise
exceptions if the input is not in range of 1-50.
"""


def make_list():
    """
    This function calls the get_input function and saves the input to a list
    :return: the completed list
    """
    user_input_list = []
    for x in range(3):
        user_input = get_input()
        if user_input.isalpha():
            raise ValueError("Input is not a number")
        elif not 0 < int(user_input) <= 50:
            raise ValueError("Input not in range 1-50")
        else:
            user_input_list.append(int(float(user_input)))
    return user_input_list


def get_input():
    """
    This function gets user input to pass to make_list
    :return: input as a string
    """
    user_input = input("Please enter a number to add to the list: ")
    return user_input


if __name__ == '__main__':
    try:
        print(make_list())
    except ValueError as error:
        print(error)

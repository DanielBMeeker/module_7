"""
Program: basic_list.py
Author: Daniel Meeker
Date: 6/19/2020

This program defines two functions, make_list and get_input
for the purpose of creating a list of user input.
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
            # used 'isalpha()' rather than 'not isnumeric()' to
            # account for the possibility of negative numbers
            raise ValueError("Input is not a number")
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

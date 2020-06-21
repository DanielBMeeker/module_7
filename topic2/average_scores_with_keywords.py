"""
Program: average_scores_with_keywords.py
Author: Daniel Meeker
Date: 6/21/2020

This program defines an average scores function that accepts both args and
kwargs to create a string that is returned to where it is called.
"""


def average_scores_kwargs(*args, **kwargs):
    """
    This function takes in 2 variable length sets of arguments, arbitrary args and
    keyword args. It uses the arbitrary args to calculate the average and the keyword
    args to display more information about the average

    :param args: variable arbitrary args to calculate average score
    :param kwargs: variable keyword args that provide more information about what is being averaged
    :return: a string combining all the key, value pairs with the calculated average
    """
    count = 0
    total = 0
    for num in args:
        total += num
        count += 1
    average = float(total) / count
    return_string = ''
    for key, value in kwargs.items():
        return_string += ("%s = %s, " % (key, value))
    return return_string + "with current average {:.2f}".format(average)


if __name__ == '__main__':
    print(average_scores_kwargs(25, 30, 35, 40, 55, student_name='Daniel Meeker', course_name='Python', current_gpa='3.9'))
    print(average_scores_kwargs(145, 185, 211, tournament_name='Val Lanes Invitational', bowler_name='Brice', previous_average_score='135.00'))
    print(average_scores_kwargs(29, 35, 33, 29, current_gpa='3.85', course_name='C++', student_name='Meeker'))

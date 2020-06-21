"""
Program: file_i_o_tuples
Author: Daniel Meeker
Date: 6/21/2020

This program creates a txt file and writes to it. After finished writing
it prints out the txt file line-by-line.
"""
import os as os
file_dir = os.path.dirname(__file__)
file_name = 'student_info.txt'


def write_to_file(args):
    """
    Open the file for appending (name your file 'student_info.txt')
    Write the tuple on one line (include any newline characters necessary)
    Close the file
    """
    try:
        f = open(file_name, 'a')
        input_list = str(args) + '\n'
        f.writelines(input_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def get_student_info(**kwargs):
    """
    Prompts the user to input as many test scores as they wish
    Stores the information (name and scores) in a tuple
    Calls the function write_to_file() sending the tuple to be written to the end of the file
    :param kwargs: key words for student name
    """
    keep_going = True
    test_scores = ""
    student_info = ""
    for key, value in kwargs.items():
        while keep_going:
            scores = input("Please enter a test score for %s, if no more scores enter 'N': " % value)
            if scores.capitalize() == 'N':
                keep_going = False
            else:
                test_scores += scores + ' '
            student_info = ("%s = %s" % (key, value))
    student_info = student_info, test_scores
    write_to_file(student_info)


def read_from_file():
    """
    Reads a file line by line
    Prints each line to the console
    """
    try:
        f = open(os.path.join(file_dir, file_name), "r")
        print(f.read())
    except IOError as e:
        print(e)
    finally:
        f.close()


if __name__ == '__main__':
    get_student_info(student_name='Daniel')
    get_student_info(student_name='Adam')
    get_student_info(student_name='Erin')
    get_student_info(student_name='Georgia')
    read_from_file()
    input('Press any key to end.')

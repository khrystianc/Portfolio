# Author: Khrystian Clark
# Date: 11/3/2020
# Description: A recursive function that finds if one string is subsequent of another
#               and returns the bool answer.

def is_subsequence(a_line, b_line):
    """Function taking in parameter of two strings and returns the bool of the subsequence, using recursion"""
    if a_line == "":  # Returns True if the A string is empty or becomes empty
        return True
    if b_line == "":  # Returns false if the B string runs out of items or is empty while the A string is not
        return False
    elif a_line[0] == b_line[0]:  # Compares the first two items in each string and gives recursion based on outcome
        return is_subsequence(a_line[1:], b_line[1:])
    elif a_line[0] != b_line[0]:
        return is_subsequence(a_line, b_line[1:])
    else:  # Any other outcome is False
        return False

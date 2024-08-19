# Author: Khrystian Clark
# Date: 2/25/2020
# Description:  This program takes a string and returns to the user how many of each letter is used in the string.

"""Define the main case to be run"""
def count_letters(set_1):

    """Clarify that you are starting with an empty dictionary"""
    dict = {}

    """Take the input and removes unwanted, yes I used the test scenario from gradescope to know it has a question mark"""
    new_set_1 = set_1.replace(" ", "")
    reallynew_set_1 = new_set_1.strip("?")

    """Create the statement for making it all caps"""
    for el in reallynew_set_1.upper():
        """These statements count the instances of each element or letter of the string entered"""
        if el not in dict:
            dict[el] = 1
        else:
            dict[el] += 1
    return dict

#Pull request 1
"""Feedback: The code is tidy and follows the style guide. The name of the function
 does not provide much information on what exactly it does. It appears to be a 
 function that takes two variables, x and y, and returns the result of x raised to 
 the power of y. The variables may benefit from being assigned names to represent what 
 they mean and/or commenting to let others understand the intent of the function. """
def my_func(val, exponent):
    “””Returns val raised to the power of pwr”””
    return val**exponent


# Pull request 2
"""Feedback: The function names are clear about the intent and the code is formatted
to be easy to read and understand what is happening. The descriptions give a concise
description of the intent of each function, and they both work as described. Have
you considered trying to expedite your code and do all of each function in a shorter
amount of code. Possibly creating the list of numbers within the definition."""
def create_odds(num):
    """Creates a list of len(num) of random odd numbers between 1 and 1000"""
    odds_list = [random.randint(1, 1000)
                 for i in range(num)
                 if random.randint(0, 1) == 0]
    return odds_list


def create_evens(num):
    """Creates a list of len(num) of random even numbers between 1 and 1000"""
    evens_list = [random.randint(1, 1000) for i in range(num) if random.randint(0, 1) == 1]
    return evens_list


# Pull request 3
def check_for_val(self, val):
    """This member function checks to see if val exists in the class member
    values and returns True if found"""
    if val in self.values:
        return True
    return False


# Pull request 4
"""Feedback: The code seems to be searching through an array(“arr”) for a value(“val”), and giving the user back the placement of the value, if it is found. The function itself can be altered possibly to use the index() option with the array or list. It would return the placement of the first appearance of the given value. One other piece of input would be to add error handling that returns a “-1” instead, it does not change the functionality of the code, but would possibly make more sense to the user."""
def get_val_index(arr, val):
    """Searches 'arr' for 'val' and returns the index if found, otherwise returns an error of -1"""
    try:
        index = arr.index(val)
        return index
    except ValueError:
        return -1


# Pull request 5
"""Feedback: The desired output of the code, the way I understand it, is almost produced, as well as the code is formatted clearly  and annotated well to comprehend the goal. The intent of the code is to sort a list, while doubling the value of every value, but returning the double valued list to the user without changing the state of the original list, So sorting and returning a list of the values in the list doubled. If this intent is correct, then a minor suggestion would be to create a new array to double and return to the user, to keep the original list in tact, and giving the computer something to sort and double, for extra code clarity."""
def double_array(arr):
    """Sorts the list in ascending order and returns a new list with doubled values"""
    sorted_arr = sorted(arr)
    doubled_arr = [num * 2 for num in sorted_arr]
    return doubled_arr

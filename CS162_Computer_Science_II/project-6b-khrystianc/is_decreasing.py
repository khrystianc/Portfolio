# Author: Khrystian Clark
# Date: 11/3/2020
# Description: A recursive function that tells you if the given list is is decreasing order
#               Returns the bool if it is decreasing or not.


def is_decreasing(num_list):
    if len(num_list) == 2 and num_list[0] > num_list[1]:
        """Re-established the assumed that the list has two or more objects
        First number on the list is greater than the next"""
        return True
    if num_list[0] >= num_list[1]:
        """Increments the starting number of list to be the next, and recursion starts"""
        return is_decreasing(num_list[1:])
    else:
        return False

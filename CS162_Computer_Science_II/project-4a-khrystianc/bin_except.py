# Author: Khrystian Clark
# Date: 10/20/2020
# Description: Modified return for target not being found in a binary list search.

class TargetNotFound(Exception):
    """Establishes the class of the exception that is to be raised."""
    pass


def bin_except(list_a, target):
    """This is the function that does the list search"""
    first = 0
    last = len(list_a) - 1
    while first <= last:
        middle = (first + last) // 2
        if list_a[middle] == target:
            return middle
        if list_a[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    raise TargetNotFound   # Raises the exception of -1 if the target is not on the list.

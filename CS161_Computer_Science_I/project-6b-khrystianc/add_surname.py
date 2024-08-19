# Author: Khrystian Clark
# Date: 2/12/2020
# Description: Takes a list of names and returns the names that start with "K" followed by Kardashian

def add_surname(names):
    """
    Given a list of names, filter for items that begin with 'K'
    and return a new list with those items suffixed with 'Kardashian'
    and a space in between.
    :param names: list of names
    :rtype: list
    :returns: list of names that begin with 'k' and have 'kardashian appended
    """
    return [name + " " + "Kardashian" for name in names if name[0].lower() == 'k']
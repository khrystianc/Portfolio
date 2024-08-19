# Author: Khrystian Clark
# Date: 10/20/2020
# Description: Program that counts the number of comparisons and exchanges that happen when a list is
#              put through a bubble sorting process.


def bubble_count(a_list):
    """Utilizes a bubble sort to sort the number of comparisons and exchanges
    returning a tuple of how many compares and exchanges occur"""
    comparisons = 0
    exchanges = 0
    for compare in range(len(a_list)):
        """Loop containing elements from 1 to list length - 1"""
        for item in range(len(a_list) - compare - 1):
            """The last elements get sorted last to ease time complexity"""
            comparisons += 1
            """Adds a sure compare to the amount of comparisons made thus far in the loop"""
            if a_list[item] > a_list[item + 1]:
                """This statement swaps the two elements returning an added exchange"""
                a_list[item] = a_list[item + 1]
                a_list[item + 1] = a_list[item]
                exchanges += 1
    return comparisons, exchanges

def insertion_count(a_list):
    """Uses an instertion sort on a given list and returns the amount
     of comparisons and exchanges that happen"""
    comparisons = 0
    exchanges = 0
    for exchange in range(1, len(a_list)):
        """Loop that begins and tracks the sort process"""
        value = a_list[exchange]
        pos = exchange - 1
        while pos >= 0 and value < a_list[pos]:
            """Loop that adds the occuring exchanges and compares to the values"""
            exchanges += 1
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            comparisons += 1
        a_list[pos + 1] = value
    return comparisons, exchanges
# Author: Khrystian Clark
# Date: 10/20/2020
# Description: Takes a list of strings and sorts it alphabetically, disregarding captitalization.


def string_sort(thinglist):
    """Method establishing that it will sort the strings in a list"""
    a_list = []
    """Establishes the empty list"""
    for thing in range(len(thinglist)):
        """This changes all strings in the list to lower cases for comparison and sorting"""
        a_list.append(thinglist[thing].lower())
    thinglist = a_list
    """Thinglist is re-established and the insertion sort is started"""
    for thing in range(1, len(thinglist)):
        """The insertion sort on the new thinglist values"""
        value = thinglist[thing]
        pro = thing
        while pro > 0 and thinglist[pro - 1] > value:
            thinglist[pro] = thinglist[pro - 1]
            pro -= 1
        return thinglist

# Author: Khrystian Clark
# Date: 2/19/2020
# Description:  This program takes a list and reverses the order of the list.

def reverse_list(val):
    for index in range(len(val)):
        val[index] = val[::-1]
    return val
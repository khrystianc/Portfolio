# Author: Khrystian Clark
# Date: 11/3/2020
# Description: A recursive function named list_max
#     that takes as its parameter a list of numbers
#     and returns the maximum value in the list.


def list_max(num_list):
    if len(num_list) == 1:
        """If there is only one item on the list return that item as the max value"""
        return num_list[0]
    elif num_list[0] > num_list[1]:
        num_list[1] = num_list[0]
        return list_max(num_list)
    else:
        return list_max(num_list[1:])

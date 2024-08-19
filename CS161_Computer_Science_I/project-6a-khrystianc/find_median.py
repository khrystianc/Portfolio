# Author: Khrystian Clark
# Date: 2/12/2020
# Description:   Program takes a list and returns the median

def find_median(arr):
    """find_median accepts a list of numbers as an
    argument, sorts the list, and finds and returns the median of the numbers."""
    arr.sort()
    length = len(arr)
    # Median of odd-numbered list
    if length % 2 != 0:
        middle_index = (length//2)
        median = arr[middle_index]
        return median
    # Median of even-numbered list
    else:
        lower_mid = (length // 2) - 1
        upper_mid = length // 2
        median = (arr[lower_mid] + arr[upper_mid]) / 2
        return median
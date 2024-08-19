# Author: Khrystian Clark
# Date: 2/19/2020
# Description:   This program takes a list and returns the squares of the elements withing the list as a list.

def square_list(nums):
    for index in range(len(nums)):
        nums[index] == [el * el for el in nums]
    return nums
# Author: Khrystian Clark
# Date: 11/4/2020
# Description: Token puzzle game where you parse a list of integers

def row_puzzle(num_list):
    if num_list[0] >= num_list[1]:
        if num_list[1] is num_list[-1]:
            if (num_list[0] - num_list[1]) > 0:
                return False
            return True
        num_list[1] = (num_list[0] - num_list[1])
        return row_puzzle(num_list[1:])
    if num_list[0] < num_list[1]:
        if num_list[1] is num_list[-1]:
            if (num_list[0] - num_list[1]) > 0:
                return False
            return True
        num_list[1] = (num_list[0] + num_list[1])
        return row_puzzle(num_list[1:])

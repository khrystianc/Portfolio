# Author: Khrystian Clark
# Date: 1/29/2020
# Description:  This program calculates a "Hailstorm" sequence based odd and even integers.
#               If even or odd, will run a specific algorithm until the algorithm ends at "1"

"""Establish a count due to the program counter starting at 0. This will help the program keep count"""
def hailstone(num):
    """
    Returns the number of steps taken to reach 1 from an initial positive number in a hailstone sequence.
    """
    count = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = ((num * 3) + 1)
        count += 1
    return count

# answer = hailstone(1000)
# print(answer)
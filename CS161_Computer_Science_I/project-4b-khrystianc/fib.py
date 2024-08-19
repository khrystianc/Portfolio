# Author: Khrystian Clark
# Date: 1/29/2020
# Description:  Takes the an positive placed integer of the Fibonacci interval and gives the output of the integer at that position.

"""If we wanted to show output, Let the user define what number step in the Fib interval they would like"""

def fib(place):
    ''' Returns the corresponding number in the fibonacci sequence to position "place" '''
    first = 1
    last = 1
    if place == 1:
        return first
    elif place == 2:
        return last
    else:
        for i in range(place-2):
            current = first + last
            first = last
            last = current
        return current
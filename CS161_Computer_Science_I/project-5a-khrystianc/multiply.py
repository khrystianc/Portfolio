# Author: Khrystian Clark
# Date: 2/5/2020
# Description:  This program takes two positive integers and returns the product of the two without using actual multiplication.

"""Defines the intended procedure, to multiply two positive integers"""
def multiply(num_1, num_2):

    """Ensures num_1 and num_2 or positive integers"""
    if num_1 <= 0 or num_2 <= 0:
        return 0

    # Recursive function which allows addition of a + b from n to 1
    # Example: (a * b) = a + (a * b-1) b times = a + (a + (a + (a))) b times.
    """Returns the original first number plus the restatement of 'multiple' with two new arguments
     changing the sewond number to support the multiplication-free multiplication"""
    return num_1 + multiply(num_1, num_2 - 1)

# Test:
# example = multiply(5, 10)
# print(example)


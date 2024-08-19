# Author: Khrystian Clark
# Date: 11/18/2020
# Description: program that makes the graphs of how long it takes to bubble sort a list of 10 random numbers
#               in increments of 1000s and returns the graphs of how long it took the function

import time
import random
from matplotlib import pyplot


def sort_timer(func):
    """Use the time module to write a decorator function named sort_timer
    that times how many seconds it takes the decorated function to run"""
    def the_timer(numbers):
        begin = time.perf_counter()
        func(numbers)
        end = time.perf_counter()
        return end - begin
    return the_timer


def bubble_sort(a_list):
    """Sorts a_list in ascending order"""
    for a in range(len(a_list) - 1):
        for b in range(len(a_list) - 1 - a):
            if a_list[b] > a_list[b + 1]:
                temp = a_list[b]
                a_list[b] = a_list[b + 1]
                a_list[b + 1] = temp


def insertion_sort(a_list):
    """Sorts a_list in ascending order"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble_func, ins_func):
    """that takes the two decorated sort functions as parameters. It should randomly generate a list of 1000
    numbers and then make a separate copy of that list."""
    bubble_nums = []
    insert_nums = []
    x_coord = []
    for i in range(1000, 10001, 1000):  # Range of 1000 to 10000 by way pf 1000s
        """The random numbers should all be integers in the range 1 <= r <= 10000."""
        list1 = [random.randint(1, 10000) for num in range(i)]
        list2 = list(list1)
        x_coord.append(i)
        bubble_nums.append(bubble_func(list1))
        insert_nums.append(ins_func(list2))
    pyplot.plot(x_coord, bubble_nums, 'ro--', linewidth=2, label="Bubble Sort")
    pyplot.plot(x_coord, insert_nums, 'go--', linewidth=2, label="Insertion Sort")
    pyplot.legend(loc="upper left")
    pyplot.show()  # The call to the show function displays the graph.

compare_sorts(bubble_sort, insertion_sort) # Call function to help grader

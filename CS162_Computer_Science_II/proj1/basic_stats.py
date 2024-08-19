# Author: Khrystian Clark
# Date: 9/28/2020
# Description: basic_stats Takes on a list of people objects with names and ages and returns the mean, median and mode of their ages.


import statistics
#  Import the statistics module


class Person:
    """This class holds two parameters of name and age. It establishes the values as private data members."""
    #  create a class called "Person"

    def __init__(self, name, age):
        """This function initializes the two data members, name and age, for the Person class"""
        self._name = name
        self._age = age

    def get_age(self):
        """This 'get' method is used to receive the age parameters from the people entered in the person list"""
        return self._age
    # create a "get_age" method to create a list of ages


def basic_stats(person_list):
    """This function takes a list of people objects as a parameter and ultimately returns a tuple containing the mean,
    median and mode of the ages"""
    age_list = []
    #  Creates a separate function "basic_stats"
    for p in person_list:
        age_list.append(p.get_age())  # This loop appends the list of ages
    mean_val = statistics.mean(age_list)
    median_val = statistics.median(age_list)
    mode_val = statistics.mode(age_list)
    return mean_val, median_val, mode_val

# Author: Khrystian Clark
# Date: 2/12/2020
# Description:   Gets a name and age. returns the standard deviation of the list of people

class Person:
    """represents a person object with name and age members"""
    def __init__(self, name, age):
        """initializes person variable based on name/age arguments passed"""
        self.name = name
        self.age = age
def std_dev(persons):
    """takes a list of people as input and returns the standard deviation of their
    ages as an output"""
    # store the mean of the ages in a variable
    cumulative_ages = 0
    for p in persons:
        cumulative_ages += p.age
    mean = cumulative_ages / len(persons)
    # store the sum of squared differences in a value
    sum_square_dif = 0
    for p in persons:
        sum_square_dif += (p.age - mean) ** 2
    return (sum_square_dif / len(persons)) ** 0.5

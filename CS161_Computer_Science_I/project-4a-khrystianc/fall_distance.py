# Author: Khrystian Clark
# Date: 1/29/2020
# Description: This program tells you the distance an object has fallen in a given amount of time.


def fall_distance(num_1):
    """gives the result equation for time and distance of the object falling by in unit if seconds based on user input"""
    if num_1 >= 0:
        return (9.8 * num_1**2) / 2
    else:
        print (0)

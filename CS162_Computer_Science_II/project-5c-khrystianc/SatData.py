# Author: Khrystian Clark
# Date: 10/27/2020
# Description: Program that reads a local json file and returns the data in a csv file format

import json
"""Imports the json module"""


class SatData:
    """Class that establishes private data members and functions to access the json
    and create the csv file"""

    def __init__(self):
        """Init method to initialize the access member of the json file"""
        with open('sat.json', 'r') as infile:
            self.__data = json.load(infile)

    def save_as_csv(self, _db_nums):
        """Method that parses the json file and creates the csv file"""
        db_data = []
        """Create an empty list for the DBNs to be stored when pulled from the json"""
        for item in self.__data:
            """For any item in the data from the json, match and add it to the DBN list if it matches"""
            if item in _db_nums:
                db_data.append(item)
        db_data.sort()
        """Sort the updated DBN list"""

        with open('output.csv', 'w') as outfile:
            """Creates the output file fir the csv created"""
            for item in db_data:
                """adds items to the outfile or the csv and creates new columns"""
                outfile.write(item['name'] + ", ")
                outfile.write('\n')
            for item in self.__data:
                """Adds elements to the csv based on their categorical data"""
                if item in _db_nums:
                    outfile.write(",".join([","+str(elem)+"," for elem in item])+"\n")
# csv is harder than i thought it would be

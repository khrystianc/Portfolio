# Author: Khrystian Clark
# Date: 10/26/2020
# Description: A class that shows the use of a json file to parse through a list of NobelData
#               and returns the sorted list of winners' surnames for that year and category.

import requests  # Not sure why import json did not work

"""Establishing of the NobelData class that will use the imported file/json"""


class NobelData:
    """Class that holds the functions to return the needed output of Nobel Data"""

    def __init__(self):
        """Initializes the get from the wanted json, and saves the read file as a private variable"""
        read_file = requests.get('http://api.nobelprize.org/v1/prize.json')
        self.__data = read_file.json()  # Loads the JSON format data

    def search_nobel(self, _year, _category):
        """The search method that uses the year and the category to parse through the
        json file for the user and returns wanted results"""
        prize_length = len(self.__data['prizes'])
        """uses the private data member from the init to store the length of the prizes"""
        winners = []
        """Establishes winners as an empty list"""
        w_sur = []
        """Established the surnames of the winners as an empty list"""

        for a in range(0, prize_length):
            """The loop that finds out if the input is equal to the year or the category and assigns a
            new item to the winners list"""
            if self.__data['prizes'][a]['year'] == _year and self.__data['prizes'][a]['category'] == _category:
                winners = self.__data['prizes'][a]['laureates']
                break
        winners_length = len(winners)
        """New vairable that calculates the length of 'winners' and stores it"""
        for b in range(0, winners_length):
            """Appends the surnames list with the added winners[b]['surname]"""
            w_sur.append(winners[b]['surname'])
        w_sur.sort()
        """Sorts the surnames list"""
        return w_sur

# Author: Khrystian Clark
# Date: 10/28/2020
# Description: project that adds/deletes/searches through the pets within a neighborhood directory.

import json
"""Import the json file"""


class NeighborhoodPets:
    """Class that holds the methods to add/delete/search the directory"""

    def __init__(self):
        """Initializes directory or set of pets in the neighborhood"""
        self.__pets = {}

    def add_pet(self, _name, _species, _owner):
        """Function that adds a pets name if it not already
        recognized in the set"""
        if _name not in self.__pets.keys():
            self.__pets[_name] = {"name": _name,
                                  "species": _species,
                                  "owner": _owner}
        else:
            return "Pet already in directory"

    def delete_pet(self, _name):
        """Deletes a pet from the library, if they are in the set"""
        if _name in self.__pets.keys():
            self.__pets.pop(_name)
        else:
            return "Pet does not exist here"

    def get_owner(self, _name):
        """Get the name of the pet owner from the library, if they are present"""
        if _name in self.__pets.keys():
            return self.__pets[_name]["owner"]
        else:
            return "Owner does not exist here"

    def save_as_json(self, _filename):
        """Function that saves the data into a json binary file"""
        with open(_filename, 'w') as outfile:
            json.dump(self.__pets, outfile)

    def read_json(self, _filename):
        """Function that reads the created json file from past information"""
        with open(_filename) as j_file:
            self.__pets = json.load(j_file)

    def get_all_species(self):
        """Gathers the species types into a set and returns the gathered set"""
        set_species = {pet['species'] for pet in self.__pets.values()}
        return set_species

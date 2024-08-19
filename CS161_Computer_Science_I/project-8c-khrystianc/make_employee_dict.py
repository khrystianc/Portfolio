# Author: Khrystian Clark
# Date: 2/25/2020
# Description:   This program creates an employee archive based on four lists of input

"""Create the class in which everything falls under with not private data members"""
class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address

    """This function takes the data members and makes them into a dictionary of the employees with the employee ID as the key"""
    def make_employee_dict(self):
        dict = {}  #establishes the empty dictionary
        """created variables for each data member in order to make it more simple to myself to test faster also creates a conounter to navigate through each list equally"""
        a = self.ID_number
        b = self.name
        c = self.salary
        d = self.email_address
        y = 0
        """for each element (i) in the kay of a which is the list od ID numbers its attribute is the combination of the employees' name, salary and email"""
        for i in a:
            dict[i] = [b[y], c[y], d[y]]
            y += 1
        return dict
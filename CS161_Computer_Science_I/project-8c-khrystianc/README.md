# project-8c

Write a class named Employee that has data members for an employee's name, ID_number, salary, and email_address (you must use those names - don't make them private).  Write a function named make_employee_dict that takes as parameters a list of names, a list of ID numbers, a list of salaries and a list of email addresses (which are all the same length).  The function should take the first value of each list and use them to create an Employee object.  It should do the same with the second value of each list, etc. to the end of the lists.  As it creates these objects, it should add them to a dictionary, where the key is the ID number and the value for that key is the whole Employee object.  The function should return the resulting dictionary.

Remember in your testing that printing an object of a user-defined class will just print out the object's type and address in memory.  You must specifically access its data members if you want to print their values.


The file must be named: make_employee_dict.py

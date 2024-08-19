# Author: Khrystian Clark
# Date: 10/26/2020
# Description: Program that takes in textfile with numbers and creates
#               a new file containing just the sum of the numbers in the original file.

def file_sum(filename):
    """The function that finds the file with numbers and
    returns a new file with the sum of the numbers"""
    end_sum = 0
    """Establish a starting point for the final sum to add up to"""

    with open(filename, 'r') as infile:
        """opens the given file and creates a ist out of the numbers in the file"""
        for line in infile:
            """Strips the extra character and makes the list of number separated by a comma"""
            print(line.strip())
            numbers = line.split(',')
            for item in numbers:
                """Adds the numbers that are now separated by a comma into the initial value
                of end_sum"""
                end_sum += float(item)

    with open('sum.txt', 'w') as outfile:
        """creates or updates the file sum.txt with just one value, the end_sum"""
        outfile.write(str(end_sum))

    infile.close()
    """Closes the infile or the initial filename"""
    outfile.close()
    """Closes the outfile or the sum.txt"""

    return end_sum

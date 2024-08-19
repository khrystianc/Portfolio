# Author: Khrystian Clark
# Date: 1/22/2020
# Description: Asks the user how many integers they want to enter.
#              Prompts user to enter that amount of integers.
#              Returns minimum and maximum for given integers.

# Define the largest and smallest numbers possible
largest = -float('inf')
smallest = float('inf')

# Prompts the user for amount of desired variables.
print("How many integers would you like to enter?")
num_1 = int(input())
while num_1 <= 0:
    print ("Please try again.")
    break

# Asks user for number inputs based on user's previously declared.
else:
    print("Please enter", num_1, "integers.")
    for num in range(0, num_1):
        num = int(input())
        # Creates new definitions of the largest and smallest based on the user input
        if largest is None or num >largest:
            largest = num
        else:
            smallest = num

# prints minimun and maximun with the min and max range of "num" inputs.
    print ("min:",  min(num, smallest))
    print ("max:", max(num, largest))

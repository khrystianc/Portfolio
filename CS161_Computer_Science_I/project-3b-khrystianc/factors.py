# Author: Khrystian Clark
# Date: 1/22/2020
# Description: Prompts user for a positive integer
#              Returns all positive factors of the integer, excluding 1 and itself

positive_integer = int(input("Please enter a positive integer: "))

# When the user enters a POSITIVE INTEGER
if positive_integer >= 0:
    print("The factors of ", positive_integer, " are:")

# find a way to get factors of positive_integer
if positive_integer >= 0:
    count = 0    # Create new variable to have a zero startpoint
    for i in range(2, positive_integer - 1):    # Range (i)ntegers start at 2 to exclude 1 and the initial integer.
        if positive_integer % i == 0:
            print(i)
            i += 1
            count += 1

# What happens if the user puts in a null or negative integer
elif positive_integer < 0:
    print("That is not a positive integer. Goodbye.")

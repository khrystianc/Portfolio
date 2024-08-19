# Author: Khrystian Clark
# Date: 1/14/2020
# Description: Asks the user for five numbers and then
#              prints out the average of the five numbers

print("Please enter five numbers.")
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
total = num_1 + num_2 + num_3 + num_4 + num_5
average = float(total / 5)
print("The average of those numbers is:")
print(average)

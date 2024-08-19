# Author: Khrystian Clark
# Date: 1/14/2020
# Description: this program calculates change dispersion of a given amount, based on coin type

print ("Please enter an amount in cents less than a dollar.")
change = int(input())
quarters = int(change / 25) # Determines number of quarters
dimes = int((change - (quarters*25)) / 10) # Determines number of dimes
nickels = int((change - (quarters*25) - (dimes*10)) / 5)  # Determines number of nickels
pennies = int(change - (quarters*25) - (dimes*10) - (nickels*5))  # Determines number of pennies
print ("Your change will be:")
print ("Q:", quarters)
print ("D:", dimes)
print ("N:", nickels)
print ("P:", pennies)


"""Alternate method""" 
print("Please enter an amount in cents less than a dollar.")
cents = int(input())     # Assigns input amount to the variable cents
print(cents)
print("Your change will be:")
print("Q:", cents // 25)
cents = cents % 25       # Determines number of cents remaining
print("D:", cents // 10)
cents = cents % 10       # Determines number of cents remaining
print("N:", cents // 5)
cents = cents % 5        # Determines number of cents remaining
print("P:", cents)
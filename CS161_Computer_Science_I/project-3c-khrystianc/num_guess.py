# Author: Khrystian Clark
# Date: 1/22/2020
# Description:  Prompts user for a number.
#               Prompts second user to guess that number and tells them if it too high or too low
#               Correct answer will tell the users how many guesses it took.

print ("Enter the number for the player to guess.")
player_1 = int(input())
print ("Enter your guess.")
player_2 = int(input())
count = 1    # Create a counter that starts at 1 since the first guess counted is "0"
while player_2 != player_1:
    if player_2 > player_1:    # If they guess too high
        print("Too high - try again:")
        player_2 = int(input())
        if player_2 == 'done':
            break
    elif player_2 < player_1:    # If they guess too low
        print("Too low - try again:")
        player_2 = int(input())
        if player_2 == 'done':
            break
    count += 1
else:    # If they guess correctly
    print("You guessed it in", count, "tries.")
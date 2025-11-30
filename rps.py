#Welcome to the program code for Rock! Paper! Scissors!
#Inspired from YouTube channel Programming with Mosh

#Main function for defining variables, calling subfunctions and producing the results through the terminal
#Array initialization obtaining options in char form
import random
'''
Rock is represented as 'r'
Paper is represented as 'p'
Scissors is represented as 's'
'''
rps = ['r', 'p', 's']

numOfTrials = 5

print("\n")
print("---------------------------------------------------------")
print("Welcome to the game of Rock! Paper! Scissors!")
print("Objective: This program will execute the game 5 times.")
print("The player with the most points after each round wins.")
print("Let's begin!!")
print("---------------------------------------------------------")
print("\n")

print("Player Modes")
print("1: User-to-User Mode")
print("2: User-to-COM Mode")
modeSel = input("First, what mode would you like to play this game?: ")
print("\n")

if modeSel == '1':
    # Add features designed for user-to-user mode
    for x in numOfTrials:

        print("Time to make a selection player 1...")
        user1 = input("Which would you want to choose: rock, paper, or scissor?: ").lower()
        print("Saving player 1's selection choice...")
        print("Thank you player 1 for making your selection.")
        print("Player 2, prepare to make your selection...")
        user2 = input("Which would you want to choose: rock, paper, or scissor?: ").lower()
        print("Saving player 1's selection choice...")
        print("Thank you player 2 for making your selection.")
        print("\n")

        print("Processing details...")
        if user1 in rps and user2 in rps:
            user2usergameDecision(user1, user2)
        else:
            print("Input error. Try again")
            print("Time to make a selection player 1...")
            user1 = input("Which would you want to choose: rock, paper, or scissor?: ").lower()
            print("Saving player 1's selection choice...")
            print("Thank you player 1 for making your selection.")
            print("Player 2, prepare to make your selection...")
            user2 = input("Which would you want to choose: rock, paper, or scissor?: ").lower()
            print("Saving player 1's selection choice...")
            print("Thank you player 2 for making your selection.")
            print("\n")

elif modeSel == '2':
    # Add features designed for user-to-COM mode
else:
    # Notify the user that the selection other than '1' or '2' will not be considered
    print("Input Error. Try re-executing this program and make appropriate selection.")
    print("Closing out of program...")

print("\n")

def user2UserGameDecision(self, user1, user2):
    self.user1 = user1
    self.user2 = user2

    
    #In the event that there's a tie between two players
    if user1 == user2:
        score1 += 0
        score2 += 0
        print("User 1: {user1}")
        print("User 2: {user2}")
        print("Tie!")
        print("\n")
    #In the event that player 1 wins and player 2 loses a point
    elif (
        (user1 == 'r' and user2 == 's') or (user1 == 'p' and user2 == 'r') or
        (user1 == 's' and user2 == 'p')
    ):
        score1 += 1
        score2 -= 1
        print("User 1: {user1}")
        print("User 2: {user2}")
        print("Player 1 wins round {numOfTrials[x]}!")
        print("\n")
    #In the event that player 2 wins and player 1 loses a point
    elif (
        (user1 == 'r' and user2 == 'p') or (user1 == 'p' and user2 == 's') or
        (user1 == 's' and user2 == 'r')
    ):
        score1 -= 1
        score2 += 1
        print("User 1: {user1}")
        print("User 2: {user2}")
        print("Player 1 wins round {numOfTrials[x]}!")
        print("\n")
            
#End of program code
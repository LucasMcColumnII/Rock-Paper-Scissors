#Welcome to the program code for Rock! Paper! Scissors!
#Inspired from YouTube channel Programming with Mosh

#Main function for defining variables, calling subfunctions and producing the results through the terminal
#Array initialization obtaining options in char form
#import math
import random


def user2UserGameDecision(user1, user2, rps):
    user1 = user1
    user2 = user2
    rps = rps
    score1 = score2 = 0
    
    #In the event that there's a tie between two players
    if user1 == user2:
        score1 += 0
        score2 += 0
        result = score1 = score2
        print(f"User 1: {user1}")
        print(f"User 2: {user2}")
        result = print("Tie!")
        print("\n")
        return result
    #In the event that player 1 wins and player 2 loses a point
    elif (
        (user1 == 'r' and user2 == 's') or (user1 == 'p' and user2 == 'r') or
        (user1 == 's' and user2 == 'p')
    ):
        score1 += 1
        score2 -= 1
        print(f"User 1: {user1}")
        print(f"User 2: {user2}")
        result=print("Player 1 wins round!")
        print("\n")
        return result
    #In the event that player 2 wins and player 1 loses a point
    elif (
        (user1 == 'r' and user2 == 'p') or (user1 == 'p' and user2 == 's') or
        (user1 == 's' and user2 == 'r')
    ):
        score1 -= 1
        score2 += 1
        print(f"User 1: {user1}")
        print(f"User 2: {user2}")
        result=print("Player 2 wins round!")
        print("\n")
        return result
    
    print("Final results")
    print("===================================")
    print(f"User 1's score: {score1}")
    print(f"User 2's score: {score2}")
    print("===================================")

def user2COMGameDecision(self, player1, com, rps):
    self.player1 = player1
    self.com = com
    self.rps = rps

    #In the event that there's a tie between two players
    if player1 == com:
        score1 += 0
        score2 += 0
        print(f"Player 1: {player1}")
        print(f"COM: {com}")
        result = print("Tie!")
        print("\n")
        return result
    #In the event that player 1 wins and player 2 loses a point
    elif (
        (player1 == 'r' and com == 's') or (player1 == 'p' and com == 'r') or
        (player1 == 's' and com == 'p')
    ):
        score1 += 1
        score2 -= 1
        print(f"Player 1: {player1}")
        print(f"COM: {com}")
        result=print("Player 1 wins round!")
        print("\n")
        return result
    #In the event that player 2 wins and player 1 loses a point
    elif (
        (player1 == 'r' and com == 'p') or (player1 == 'p' and com == 's') or
        (player1 == 's' and com == 'r')
    ):
        score1 -= 1
        score2 += 1
        print(f"Player 1: {player1}")
        print(f"COM: {com}")
        result=print("COM wins round!")
        print("\n")
        return result
    
    print("Final results")
    print("===================================")
    print(f"Player's score: {score1}")
    print(f"COM's score: {score2}")
    print("===================================")

if __name__ == "__main__":
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
        for x in range(numOfTrials):
            while True:
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
                    user2UserGameDecision(user1, user2, rps)
                    break
                else:
                    print("Input error. Try again")
    
    elif modeSel == '2':
        # Add features designed for user-to-COM mode
        for x in range(numOfTrials):
            while True:
                print("Time to make a selection player 1...")
                player1 = input("Which would you want to choose: rock, paper, or scissor?: ").lower()
                print("Saving player 1's selection choice...")
                print("Thank you player 1 for making your selection.")
                print("COM player, prepare to make your selection...")
                com = random.choice(rps).lower()
                print("Saving COM's selection choice...")
                print("Thank you COM for making your selection.")
                print("\n")

                print("Processing details...")
                if player1 in rps and com in rps:
                    user2COMGameDecision(player1, com, rps)
                    break
                else:
                    print("Input error. Try again")
    else:
        # Notify the user that the selection other than '1' or '2' will not be considered
        print("Input Error. Try re-executing this program and make appropriate selection.")
        print("Closing out of program...")

    print("\n")

#End of program code
#Welcome to the program code for Rock! Paper! Scissors!
#Inspired from YouTube channel Programming with Mosh

#Main function for defining variables, calling subfunctions and producing the results through the terminal
#Array initialization obtaining options in char form
import math
import random

class RPS():

    def __init__(self, score1, score2, playerScore, comScore):
        self.score1=score1
        self.score2=score2
        self.playerScore=playerScore
        self.comScore=comScore

    #For two local players only (Decrementing & Incrementing)
    def incrementScore1(self):
        self.score1 += 1
        print(f"User 1's score: {self.score1}")

    def incrementScore2(self):
        self.score2 += 1
        print(f"User 2's score: {self.score2}")

    def decrementScore1(self):
        self.score1 -= 1
        print(f"User 1's score: {self.score1}")

    def decrementScore2(self):
        self.score2 -= 1
        print(f"User 2's score: {self.score2}")


    #For two local players only (When there's a tie)
    def noNewPoints(self):
        return print(f"User 1's score remains: {self.score1}\nUser 2's score remains: {self.score2}")


    #For user and com players only (Decrementing & Incrementing)
    def incrementPlayer1(self):
        self.playerScore += 1
        print(f"Player's score: {self.playerScore}")

    def decrementPlayer1(self):
        self.playerScore -= 1
        print(f"Player's score: {self.playerScore}")

    def incrementCOM(self):
        self.comScore += 1
        print(f"COM's score: {self.comScore}")

    def decrementCOM(self):
        self.comScore -= 1
        print(f"COM's score: {self.comScore}")

    #For user and COM players only (When there's a tie)
    def noNewPoints2(self):
        return print(f"Player's score remains: {self.playerScore}\n COM's score remains: {self.comScore}")

    def user2UserGameDecision(self, user1, user2, rps):
        self.user1 = user1
        self.user2 = user2
        self.rps = rps
    
        #In the event that there's a tie between two players
        if user1 == user2:
            print(f"User 1: {user1}")
            print(f"User 2: {user2}")
            result = print("Tie!")
            RPS.noNewPoints(self)
            print("\n")
            return result
        #In the event that player 1 wins and player 2 loses a point
        elif (
            (user1 == 'r' and user2 == 's') or (user1 == 'p' and user2 == 'r') or
            (user1 == 's' and user2 == 'p')
        ):
            print(f"User 1: {user1}")
            print(f"User 2: {user2}")
            result=print("Player 1 wins round!")
            RPS.incrementScore1(self)
            RPS.decrementScore2(self)
            print("\n")
            return result
        #In the event that player 2 wins and player 1 loses a point
        elif (
            (user1 == 'r' and user2 == 'p') or (user1 == 'p' and user2 == 's') or
            (user1 == 's' and user2 == 'r')
        ):
            print(f"User 1: {user1}")
            print(f"User 2: {user2}")
            result=print("Player 2 wins round!")
            RPS.incrementScore2(self)
            RPS.decrementScore1(self)
            print("\n")
            return result

    def user2COMGameDecision(self, player1, com, rps):
        self.player1=player1
        self.com=com
        self.rps = rps
    
        #In the event that there's a tie between two players
        if player1 == com:
            print(f"Player 1: {player1}")
            print(f"COM: {com}")
            result = print("Tie!")
            RPS.noNewPoints2(self)
            print("\n")
            return result
        #In the event that player 1 wins and player 2 loses a point
        elif (
            (player1 == 'r' and com == 's') or (player1 == 'p' and com == 'r') or
            (player1 == 's' and com == 'p')
        ):
            print(f"Player 1: {player1}")
            print(f"COM: {com}")
            result=print("Player 1 wins round!")
            RPS.incrementPlayer1(self)
            RPS.decrementCOM(self)
            print("\n")
            return result
        #In the event that player 2 wins and player 1 loses a point
        elif (
            (player1 == 'r' and com == 'p') or (player1 == 'p' and com == 's') or
            (player1 == 's' and com == 'r')
        ):
            print(f"Player 1: {player1}")
            print(f"COM: {com}")
            result=print("COM wins round!")
            RPS.decrementPlayer1(self)
            RPS.incrementCOM(self)
            print("\n")
            return result

if __name__ == "__main__":
    '''
    Rock is represented as 'r'
    Paper is represented as 'p'
    Scissors is represented as 's'
    '''
    rps = ['r', 'p', 's']

    numOfTrials = 5
    sumScore1=sumScore2=sumPlayer=sumCOM=0

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
        score1=score2=playerScore=comScore=0
        rocPapSci = RPS(score1, score2, playerScore, comScore)
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
                    rocPapSci.user2UserGameDecision(user1, user2, rps)
                    break
                else:
                    print("Input error. Try again")

        print("Finalizing results...")
        print("========================================================")
        print(f"User 1's final score: {rocPapSci.score1}")
        print(f"User 2's final score: {rocPapSci.score2}")
        print("========================================================")
    
    elif modeSel == '2':
        # Add features designed for user-to-COM mode
        score1=score2=playerScore=comScore=0
        rocPapSci = RPS(score1, score2, playerScore, comScore)
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
                    rocPapSci.user2COMGameDecision(player1, com, rps)
                    break
                else:
                    print("Input error. Try again")

        print("Finalizing results...")
        print("========================================================")
        print(f"Player's final score: {rocPapSci.playerScore}")
        print(f"COM's final score: {rocPapSci.comScore}")
        print("========================================================")

    else:
        # Notify the user that the selection other than '1' or '2' will not be considered
        print("Input Error. Try re-executing this program and make appropriate selection.")
        print("Closing out of program...")

    print("\n")

#End of program code
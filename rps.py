#Welcome to the program code for Rock! Paper! Scissors!

#Main function for defining variables, calling subfunctions and producing the results through the terminal
#Array initialization obtaining options in char form
import random
'''
Rock is represented as 'r'
Paper is represented as 'p'
Scissors is represented as 's'
'''
rps = ['r', 'p', 's']

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

if modeSel == '1':
    # Add features designed for user-to-user mode
elif modeSel == '2':
    # Add features designed for user-to-COM mode

print("\n")
#End of program code
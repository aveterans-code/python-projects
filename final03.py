"""
Program name: final03.py
Program Description: Number guessing game
Author: Geoff King
Date Created: May 5, 2024

Notes: Imports the python time library

"""
import time
from random import randrange

def main():
    # Print intro
    print("This program will select a random number 1-100.")
    print("Enter a number and you will get a 'higher' or 'lower' hint.")

    # Assigns rn a random number between 1 and 100
    rn = randrange(1,101)

    print("\nThe random number has been selected.")

    # A boolean loop that stays true until the guess = random number
    while True:

        guess = int(input("Your guess?: "))

        # If the guess is too high
        if guess > rn:
            #prints lower.
            print("Lower.")

        # If the guess is too low
        elif guess < rn:
            #prints higher.
            print("Higher.")

        # A correct guess
        else:
            print("Correct!")
            # Exits the loop
            break

    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

if __name__ == '__main__':
    main()

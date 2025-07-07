"""
Program name: ch5ex04.py
Program Description: Acronym builder
Author: Geoff King
Date Created: February 15, 2024

Notes: Uses the python time library

"""
import time

def main():
    print("This program builds acronyms")

    #ask the user for input 'phrase'
    phrase = input("Enter a phrase to recieve an accronym: ")
    print("The acronym is: ", end = "")

    #takes the first letter of each word and makes it uppercase
    for word in phrase.split():
        #returns the acronym to the user
        print(word[0].upper(), end = "")

    print()
    
    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ch5ex04.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

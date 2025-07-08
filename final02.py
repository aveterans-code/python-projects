"""
Program name: final02.py
Program Description: Word storage and manipulation
Author: Geoff King
Date Created: May 5, 2024

Notes: Imports the python time library

"""
import time

def main():
    # Print intro
    print("This program prints the number of words entered and")
    print("then prints out the first and last letters of each")
    print("word along with each word entered")
    print("Press Enter after each word\n")

    count = 0
    # Creates an empty list called words
    Words = ""
    # Get the first word from the user
    a = input("Enter a word or press <Enter> to Quit: ")
    Words += a

    # Loop to get words from the user until they press Enter
    while a != "":
        # Separate each word with ,
        Words+= ','
        a = input("Enter a word or press <Enter> to Quit: ")
        Words += a
        count += 1

    # Remove the last empty entry from the list
    Words = Words[:-1]
    print((count),"Words were entered")

    # Iterate over each word and prints in desired layout
    for word in Words.split(","):
        print(word[0], word[-1], word.upper())

    #adds a dividing line
    print("\n-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

if __name__ == '__main__':
    main()


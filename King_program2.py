"""
Program name: King_program2.py
Program Description: calculates the time a photo takes from Mars to NASA
Author: Geoff King
Date Created: February 8, 2024

Notes: Uses the python time library

"""
import time

def main():
    #prints a program introduction
    print("This program calculates the time it takes to send a photo from Mars to NASA\n")

    #creates a 3 iteration for loop
    for i in range(3):

        #queries user for the distance between Mars and Earth and assigns that value to distance
        distance = eval(input("Please enter the distance between Mars and Earth: "))

        #calculates the time for the photo to travel and assigns that value to t
        sec = distance / 186000

        #prints the time in seconds
        print("It will take", sec, "seconds for the photo to travel to NASA.\n")
        
    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 King_program2.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

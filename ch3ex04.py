"""
Program name: ch3ex04.py
Program Description: Calculate the distance of a lightning strike
Author: Geoff King
Date Created: February 9, 2024

Notes: Uses the python time library

"""
import time

def main():
    print("This program calculates the distance of a lightning strike.")
    print()

    t = int(input("Please enter the number of seconds between flash and thunder: "))

    f = 1100 * t
    m = f/5280
    print()

    print("The lightning is approximately", round(m, 1), "miles away.")

    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ch3ex04.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

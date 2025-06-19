"""
Program name: King_program3.py
Program Description: Calculates exponential values
Author: Geoff King
Date Created: February 12, 2024

Notes: Uses the python time and math library's
    Uses simultaneous assignment and math.pow
"""
import time
import math

def main():
    #prints a program introduction followed by an empty line
    print("This program calculates exponential values\n")

    #prompts user for number of calculations
    n = int(input("Enter the number of calculations you would like to do: "))

    #creates a counted loop which will iterate n timees
    for i in range(n):

        #prompts user for problems to be solved
        x,y = eval(input("Enter the base number followed by a comma, a space, then the exponent: "))

        #calculates the solution of x raised to the power of y
        result = math.pow(x,y)

        #prints the solution followed by an empty line
        print(x, "to the", y, "power equals:", result, "\n")
    
    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 King_program3.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

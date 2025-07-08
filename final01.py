"""
Program name: final01.py
Program Description: Use nested loops to create a table
Author: Geoff King
Date Created: May 5, 2024

Notes: Imports the python time library

"""
import time

def main():
    # Print intro
    print("This program creates a table with dimensions of the number you enter")
    # Get user input for the number
    n = int(input("Enter a number: "))
    a = 1
    # Prints header with spaces
    print("     ", end=" ")
    # Outer loop to print the header row
    while a <= n:
        print(f"{a:>3}", end=" ")
        a = a+1

    b = 0
    # Prints separator line
    print(f"\n{"----"*n}---------", end = " ")
    # Outer loop to iterate rows
    for i in range(n):
        b += 1
        # Prints row number
        print(f"\n {b:>2} |", end = " ")
        # Inner loop to iterate columns
        for i in range(1, n+1):
            x = i*b
            # Print the product of each row and column
            print(f"{x:>3}", end = " ")
    
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


"""
Program name: CIS_110 King_ch5ex11.py
Program Description: Improved chaos program
Author: Geoff King
Date created: March 14, 2024
"""

#Imports time
import time

def main():
    print("This program illustrates a chaotic function\n")
    
    x1 = float(input("Enter the first seed between 0 and 1: "))
    x2 = float(input("Enter the second seed between 0 and 1: "))
    print()
    #provides the top of the table
    print("index   ", x1, "    ", x2)
    #separating line
    print("------------------------------")
    for i in range(1, 11):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        #returns to the user with the specified spacing
        print(f'{i:2} {x1:14.6f} {x2:9.6f}')
    
    #Adds a dividing line
    print("-------------------------------")
    #Prints Author's name & course number
    print("Geoffrey King")
    print("CIS 110")
    #Prints the current date and time
    print(time.ctime())
    #Adds a dividing line
    print("-------------------------------")

main()

"""
Program name: King_Program1.py
Program Description: Hello and welcome
Author: Geoff King
Date Created: January 31, 2024

Notes: Uses the python time library

"""
import time

def main():
    #Asks user for their name and assigns the value to n
    n = input("Hi! What is your name? ")
    #Prints a greeting with the entered name
    print("Hello", n, "welcome to Programming Fundamentals!")
    
    #Adds a dividing line
    print("-------------------------------")
    #Prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 Program 1")
    #Prints the current date and time
    print(time.ctime())
    #Adds a dividing line
    print("-------------------------------")

main()

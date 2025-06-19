"""
Program name: ch2ex10.py
Program Description: A program to convert kilometers to miles
Author: Geoff King
Date Created: February 8, 2024

Notes: Uses the python time library

"""
import time

def main():
    k = eval(input("Enter the distance in kilometers: "))
    m = k * 0.62
    print(k, "kilometers equals", m, "miles.")
    
    #Adds a dividing line
    print("-------------------------------")
    #Prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ch2ex10.py")
    #Prints the current date and time
    print(time.ctime())
    print("-------------------------------")

main()

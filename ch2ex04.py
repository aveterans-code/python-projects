"""
Program name: King_ch2ex04.py
Program Description: program to convert five Celsius temps to Fahrenheit
Author: Geoff King
Date Created: February 8, 2024

Notes: Uses the python time library

"""
import time

def main():
    print("This program converts five Celsius temperatures to Fahrenheit.")
    print()

    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()

    input("Press the <Enter> key to quit.")

    #Adds a dividing line
    print("-------------------------------")
    #Prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ch2ex04.py")
    #Prints the current date and time
    print(time.ctime())
    #Adds a dividing line
    print("-------------------------------")

main()

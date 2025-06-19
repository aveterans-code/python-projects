"""
Program name: ch3ex16.py
Program Description: Calculates nth Fibonacci number
Author: Geoff King
Date Created: February 12, 2024

Notes: Uses the python time library

"""
import time

def main():
    print("This program calculates the nth Fibonacci value")

    #provides an empty line for easier reading
    print()

    n = int(input("Enter the value of n: "))
    print()

    #sets these tracking variable values to one using simultaneous assignment
    prev, curr = 1, 1
    #demonstrates a for loop with an accumulator pattern
    for i in range(n - 2):
        #simultaneous assignment and combining values
        prev, curr = curr, curr + prev
           
    #prints the value of the nth fibonacci value
    print("The nth value is:", curr)

    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ch3ex16.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

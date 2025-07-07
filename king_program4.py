"""
Program name: King_program4.py
Program Description: converts a string in a text file to numbers, then-
-converts each number to its ASCII letter, making words out of numbers
Author: Geoff King
Date Created: March 21, 2024

Notes: Uses the python time library

"""
import time

def main():
    #prints an introduction and a blank line
    print("This program converts ASCII numbers to their letter values\n")

    #prompts user for file name
    fname = input("Enter file name: ")
    
    #opens file in read mode
    infile = open(fname, "r")
    
    #reads entire file and stores it as variable string1
    string1 = infile.read()
    
    #closes file
    infile.close()
    
    #creates a blank list named poem
    poem = ""

    #loop that splits string1 at spaces
    for numStr in string1.split():

        #changes each number in the string1 to integers
        string1Num = int(numStr)
        
        #converts each integer number to its character value and adds it to poem
        poem = poem + chr(string1Num)

    #prints the converted poem, then the "end" and an additional print
    print(poem, end='')
    print()

    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 King_program4.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

"""
Program name: king_program5.py
Program Description: takes numbers input by user and squares them
Author: Geoff King
Date Created: April 8, 2024

Notes: Uses the python time and math libraries

"""
#makes time and math libraries available
import time, math

#creates function square with parameter nums
def square(nums):

    #loop based on the length of nums which will be a list
    for i in range(len(nums)):

        #squares each value of nums in place
        nums[i]= (nums[i])**2

def main():
    #intro
    print("This program will square a specified list of numbers\n")
    
    #prompts the user for the numbers they want to square and assigns to n
    n = int(input("How many numbers would you like to square? "))

    #declare nums and assign it a list with n numbers
    nums = list(range(1,n+1))

    #print the original list
    print("The original list:", nums)

    #create a counted for loop (3)
    for i in range(3):

        #call the square function which changes the value in nums
        square(nums)

        #print the updated list each iteration
        print("The updated list: ", nums) 
    
    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 program5.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

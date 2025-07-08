"""
Program name: king_program7.py
Program Description: Windchill
Author: Geoff King
Date Created: April 15, 2024

Notes: Imports the python time library

"""
import time

#creates windChill(t,v) function
def windChill(t,v):
    if v <= 3:
        #sets windchill variable equal to t if v is less than 3
        windchill = t
        return int(windchill)
    #if windchill > 3, then the below formula is used
    else:
        windchill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
        #returns calculated windchill as an int
        return int(windchill)

#creates the main function    
def main():
    #print intro
    print("Wind Chill Table")
    #prints formatted Temperature header
    print("{0:>30}".format('Temperature'))
    #first line of table
    print("MPH| {0:>5} {1:>5} {2:>5} {3:>5} {4:>5} {5:>5} {6:>5} {7:>5} {8:>5}".format(-20,-10,0,10,20,30,40,50,60))
    #adds a dividing line
    print("------------------------------------------------------------------")
    #creates the 'outer' for loop that iterates through the MPH range
    for y in range(0,55,5):
        #prints the current iteration of i (MPH)
        print("\n{0:>2}".format(y), end=" ")
        #print a separator after MPH value
        print("|", end=" ")
        #creates 'inner' for loop that iterates through the temperature range
        for z in range(-20,70,10):
            #initiates/calls the windChill function with temp and velocity variables
            windchill = windChill(z,y)
            #prints the return on windChill
            print("{0:>5}".format(windchill), end=" ")
        
        
    #adds a dividing line
    print("\n-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("---------------------------------")

main()

"""
Program name: king_program8.py
Program Description: Tic-Tac-Toe
Author: Geoff King
Date Created: April 24, 2024

Notes: Imports the python time and graphics library

"""
import time
from graphics import *

#creates graphics window called Tic-Tac-Toe 500 by 500 pixels
win=GraphWin("Tic-Tac-Toe", 500,500)
#sets window coordinate system
win.setCoords(0,0,10,10)
#sets background of window to light green
win.setBackground('light green')
#creates a 3x3 grid of individual squares
Rectangle(Point(2,2), Point(4,4)).draw(win)
Rectangle(Point(2,4), Point(4,6)).draw(win)
Rectangle(Point(2,6), Point(4,8)).draw(win)
Rectangle(Point(4,2), Point(6,4)).draw(win)
Rectangle(Point(4,4), Point(6,6)).draw(win)
Rectangle(Point(4,6), Point(6,8)).draw(win)
Rectangle(Point(6,2), Point(8,4)).draw(win)
Rectangle(Point(6,4), Point(8,6)).draw(win)
Rectangle(Point(6,6), Point(8,8)).draw(win)

#creates playx function
def playx():
    #intro message with red text for X
    message = Text(Point(5,1),"Click a square for 'X'")
    message.setTextColor('red')
    message.draw(win)
    #waits for user click
    p1= win.getMouse()
    #nested if...elif uses x coordinate from p1 to place X
    if p1.getX() > 2 and p1.getX()< 4:
        #uses y coordinate from p1 to place X
        if p1.getY() > 2 and p1.getY()< 4:
            x= Text(Point(3,3), 'X')
        elif p1.getY() > 4 and p1.getY()< 6:
            x= Text(Point(3,5), 'X')
        elif p1.getY() > 6 and p1.getY()< 8:
            x= Text(Point(3,7), 'X')

    #uses x coordinate from p1 to place X
    elif p1.getX() > 4 and p1.getX()< 6:
        #uses y coordinate from p1 to place X
        if p1.getY() > 2 and p1.getY()< 4:
            x= Text(Point(5,3), 'X')
        elif p1.getY() > 4 and p1.getY()< 6:
            x= Text(Point(5,5), 'X')
        elif p1.getY() > 6 and p1.getY()< 8:
            x= Text(Point(5,7), 'X')

    #uses x coordinate from p1 to place X
    elif p1.getX() >6 and p1.getX()< 8:
        #uses y coordinate from p1 to place X
        if p1.getY() > 2 and p1.getY()< 4:
            x= Text(Point(7,3), 'X')
        elif p1.getY() > 4 and p1.getY()< 6:
            x= Text(Point(7,5), 'X')
        elif p1.getY() > 6 and p1.getY()< 8:
            x= Text(Point(7,7), 'X')

    #sets message to blank
    message.setText("")
    #returns x
    return x

#creates playo function
def playo():
    #intro message default color
    message = Text(Point(5,1),"Click a square for 'O'")
    message.draw(win)
    #waits for user click
    p2 = win.getMouse()
    #nested if...elif uses x coordinate from p1 to place O
    if p2.getX() >2 and p2.getX()< 4:
        #uses y coordinate from p1 to place O
        if p2.getY() >2 and p2.getY()< 4:
            o= Text(Point(3,3), 'O')
        elif p2.getY() >4 and p2.getY()< 6:
            o= Text(Point(3,5), 'O')
        elif p2.getY() >6 and p2.getY()< 8:
            o= Text(Point(3,7), 'O')
    #uses x coordinate from p1 to place O
    elif p2.getX() >4 and p2.getX()< 6:
        #uses y coordinate from p1 to place O
        if p2.getY() > 2 and p2.getY()< 4:
            o= Text(Point(5,3), 'O')
        elif p2.getY() > 4 and p2.getY()< 6:
            o= Text(Point(5,5), 'O')
        elif p2.getY() > 6 and p2.getY()< 8:
            o= Text(Point(5,7), 'O')
    #uses x coordinate from p1 to place O
    elif p2.getX() >6 and p2.getX()< 8:
        #uses y coordinate from p1 to place O
        if p2.getY() > 2 and p2.getY()< 4:
            o= Text(Point(7,3), 'O')
        elif p2.getY() > 4 and p2.getY()< 6:
            o= Text(Point(7,5), 'O')
        elif p2.getY() > 6 and p2.getY()< 8:
            o= Text(Point(7,7), 'O')
        
    #sets message to blank
    message.setText("")
    #returns o
    return o

#creates main function
def main():
    #sets a blank message
    message = Text(Point(5,1),"")
    #initiates the first turn of playx function
    x = playx()
    #set text color to red for X
    x.setTextColor('red')
    #draws returned text from playx function
    x.draw(win)
    #creates a counted for loop 4x ( makes eight turns )
    for i in range(4):
        #initiates/iterates the playo function
        o = playo()
        #draws returned text from playo function
        o.draw(win)
        #iterates the playx function
        x = playx()
        #set text color to red for X
        x.setTextColor('red')
        #draws returned text from playx function
        x.draw(win)

    #exit message
    message.setText("Click to close")
    #print exit message
    message.draw(win)
    #waits for a click
    win.getMouse()
    #closes window
    win.close()

#adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 king_program8.py")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")
main()

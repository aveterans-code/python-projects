#ch4ex11.py

from graphics import *

def main():

    win = GraphWin('Draw a House below', 500,500)
    win.setCoords(0,0,200,200)
    message = Text(Point(100,5),"")
    message.draw(win)

    # Draw house frame
    message.setText("Click on lower left corner of the frame")
    p1 = win.getMouse()
    p1.draw(win)
    message.setText("Click upper right corner of the frame")
    p2 = win.getMouse()
    house = Rectangle(p1,p2)
    house.setFill('gray')
    house.draw(win)

    # Draw a door
    houseWidth = p2.getX() - p1.getX()
    doorWidth = 0.16 * houseWidth
    message.setText("Click upper right corner of the door")
    p3 = win.getMouse()
    doorBL = Point(p3.getX() - doorWidth, p1.getY())
    door = Rectangle(p3, doorBL)
    door.setFill('light blue')
    door.draw(win)

    # Draw the roof
    message.setText("Click on the peak of the roof")
    p5 = win.getMouse()
    roof = Polygon(Point(p1.getX(), p2.getY()), p5, p2)
    roof.setFill('red')
    roof.draw(win)

    # Draw a window
    message.setText("Click on the center of the window")
    p4 = win.getMouse()
    window = Circle(p4, 0.5 * doorWidth)
    window.setFill('teal')
    window.draw(win)

    #Draw a second window ( for fun )
    message.setText("Click on the center of the window")
    p6 = win.getMouse()
    window1 = Circle(p6, 0.5 * doorWidth)
    window1.setFill('teal')
    window1.draw(win)

    # Click to close
    message.setText("Click to close program.")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

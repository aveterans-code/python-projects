#ch4ex03.py

from graphics import *

def main():

    win = GraphWin('Portrait', 400,400)
    win.setBackground('white')

    head = Oval(Point(100,60), Point(320,350)).draw(win)
    head.setFill('tan')

    leye = Oval(Point(135,154), Point(174,175))
    leye.setFill('white')
    leye.draw(win)

    reye=leye.clone()
    reye.move(100,0)
    reye.draw(win)

    lpupil = Circle(Point(150,165),7)
    lpupil.setFill('light blue')
    lpupil.draw(win)

    rpupil = lpupil.clone()
    rpupil.move(100,0)
    rpupil.draw(win)

    lpupil2 = Circle(Point(150,165),2)
    lpupil2.setFill('black')
    lpupil2.draw(win)

    rpupil2 = lpupil2.clone()
    rpupil2.move(100,0)
    rpupil2.draw(win)

    nose1 = Polygon(Point(210,180), Point(195,205), Point(205,220))
    nose1.setFill('tan')
    nose1.draw(win)
                    #top            bleft           bright
    nose = Polygon(Point(195,205), Point(182,225), Point(208,225))
    nose.setFill('tan')
    nose.draw(win)

    lnostril = Circle(Point(185,222),5)
    lnostril.setFill('black')
    lnostril.draw(win)

    rnostril = Circle(Point(205,222),5)
    rnostril.setFill('black')
    rnostril.draw(win)

    smile = Oval(Point(160,290), Point(240,280))
    smile.setFill('black')
    smile.setOutline(color_rgb(238,193,173))
    smile.setWidth(8)
    smile.draw(win)

    message = Text(Point(100,350),"")
    message.setText("Click to close")
    message.draw(win)
    win.getMouse()
    win.close()

main()

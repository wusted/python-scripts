#!/usr/bin/python3


import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    fillbar(t, height)
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(5)
    if height >= 0:
        t.write(str(height), align="center")
    t.forward(35)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def fillbar(t, height):
    """ Set the fillcolor for t, depending on height. """
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    elif height >= 0 and height < 100:
        t.fillcolor("green")
    elif height < 0 and height >= -100:
        t.fillcolor("lightblue")
    elif height < -100 and height >= -200:
        t.fillcolor("blue")
    elif height < -200:
        t.fillcolor("purple")
    t.begin_fill()

xs = [ -48,  117,  200,  -240,  160,  -160,  90]  # here is the data
maxheight = max(xs)
minheight =min(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
if minheight > 0:
    lly = 0
else:
    lly = minheight - border
wn.setworldcoordinates(0-border, lly, 40*numbars+border, maxheight+border)

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)



for a in xs:
    drawBar(tess, a)

wn.exitonclick()

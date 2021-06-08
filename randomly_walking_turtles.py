#!/usr/bin/python3

import turtle
import random

def isInScreen(w, t):
    leftBound = - wn.window_width() / 2
    rightBound = wn.window_width() / 2
    bottomBound = - wn.window_height() / 2
    topBound = wn.window_height() / 2
    
    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX < leftBound or turtleX > rightBound:
        stillIn = False
    if turtleY < bottomBound or turtleY > topBound:
        stillIn = False

    return stillIn
    
t = turtle.Turtle()
wn = turtle.Screen()

t.shape("turtle")
while isInScreen(wn , t):
    coin = random.randrange(0,2)
    if coin == 0:       # heads
        t.left(90)
    else:
        t.right(90)
    
    t.forward(50)

wn.exitonclick()
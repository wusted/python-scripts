#!/bin/python3

import turtle

def drawSpiral(t, angle, reps):
    """ takes turtle t, and an angle in degrees. """
    length = 1
    for i in range(reps):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()       # Set up window and it's attributes
wn.bgcolor("lightgreen")

jean = turtle.Turtle()
jean.color("blue")

# draw the first spiral ##
# position jean
jean.penup()
jean.backward(110)
jean.pendown()
jean.speed(120)

reps = 45
angle = 90
# draw the spiral using a 90 degree turn angle
drawSpiral(jean, angle, reps)

## draw the second spiral ##
# positon jean
jean.penup()
jean.home()
jean.forward(90)
jean.pendown()

reps = 100
angle = 89
drawSpiral(jean, angle, reps)

wn.exitonclick()
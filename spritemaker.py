#!/usr/bin/python3

import turtle

def drawSprite(turtle, numlegs, lenlegs):
    """ this will draw sprite with turtle, using numlegs, lenlegs and angle variables """
    turtle.shape("triangle")
    angle = 360/numlegs
    for i in range(numlegs):
        # draw the leg
        turtle.right(angle)
        turtle.forward(lenlegs)
        turtle.stamp()

        # go back to the middle and turn back around
        turtle.right(180)
        turtle.forward(lenlegs)
        turtle.right(180)

wn =  turtle.Screen()
wn.bgcolor("lightblue")

jean = turtle.Turtle()
jean.speed(75)

num = int(input("How many legs should this sprite have? "))
size = int(input("How long should each leg be? ")) 

drawSprite(jean, num, size)
jean.shape("circle")

wn.exitonclick()
